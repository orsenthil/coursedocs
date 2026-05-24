#!/usr/bin/env python3
"""Extract external URLs from gatech RST docs, publish to Linkding, strip from source."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

LINKDING_BASE = "https://links.learntosolveit.com"
TAG = "courses"
ROOT = Path(__file__).resolve().parents[1]
GATECH = ROOT / "gatech"

# --- extraction patterns -------------------------------------------------------

RST_REF_DEF = re.compile(r"^(\.\.\s+_([^:]+):\s+)(https?://\S+)\s*$", re.M)
RST_REF_USE = re.compile(r"`([^<`]+)`_")
RST_INLINE = re.compile(r"`([^<`]+)\s*<([^>]+)>`_")
MARKDOWN_LINK = re.compile(r"\[([^\]]+)\]\((https?://[^\)]+)\)")
BARE_URL = re.compile(r"https?://[^\s\)\]\"'<>]+")
HTML_IFRAME = re.compile(
    r"<iframe[^>]*src=\"(https?://[^\"]+)\"[^>]*>.*?</iframe>", re.S | re.I
)
HTML_OBJECT = re.compile(
    r"<object[^>]*data=\"(https?://[^\"]+)\"[^>]*>.*?</object>", re.S | re.I
)
HTML_A = re.compile(r'<a\s+href="(https?://[^"]+)"[^>]*>([^<]*)</a>', re.I)
IMAGE_EXT = re.compile(r"^\.\.\s+image::\s+(https?://\S+)", re.M)
RAW_HTML_BLOCK = re.compile(r"\.\. raw:: html\s*\n(?:\s+.*\n)+", re.M)


@dataclass
class LinkEntry:
    url: str
    title: str
    source: str
    notes: str = ""


@dataclass
class ExtractResult:
    links: list[LinkEntry] = field(default_factory=list)
    seen_urls: set[str] = field(default_factory=set)


def normalize_url(url: str) -> str:
    return url.rstrip(".,;:)")


def add_link(result: ExtractResult, url: str, title: str, source: str, notes: str = "") -> None:
    url = normalize_url(url)
    if not url.startswith(("http://", "https://")):
        return
    if url not in result.seen_urls:
        result.seen_urls.add(url)
        result.links.append(LinkEntry(url=url, title=title or url, source=source, notes=notes))


def extract_from_file(path: Path) -> ExtractResult:
    rel = str(path.relative_to(ROOT))
    text = path.read_text(encoding="utf-8", errors="replace")
    result = ExtractResult()

    for m in RST_REF_DEF.finditer(text):
        add_link(result, m.group(3), m.group(2).strip(), rel)

    for m in RST_INLINE.finditer(text):
        add_link(result, m.group(2), m.group(1).strip(), rel)

    for m in MARKDOWN_LINK.finditer(text):
        add_link(result, m.group(2), m.group(1).strip(), rel)

    for m in HTML_IFRAME.finditer(text):
        add_link(result, m.group(1), "Embedded video", rel)

    for m in HTML_OBJECT.finditer(text):
        add_link(result, m.group(1), "Embedded PDF", rel)

    for m in HTML_A.finditer(text):
        add_link(result, m.group(1), m.group(2).strip() or m.group(1), rel)

    for m in IMAGE_EXT.finditer(text):
        add_link(result, m.group(1), "External image", rel)

    for m in BARE_URL.finditer(text):
        url = normalize_url(m.group(0))
        # skip if already captured as part of ref def on same line
        line_start = text.rfind("\n", 0, m.start()) + 1
        line = text[line_start : text.find("\n", m.start()) if "\n" in text[m.start():] else len(text)]
        if re.search(r"\.\.\s+_", line):
            continue
        if re.search(r"`[^<`]*<" + re.escape(url), line):
            continue
        if re.search(r"\]\(" + re.escape(url), line):
            continue
        # derive title from bullet prefix if present
        title = url
        bullet = re.match(r"^\s*[\*\-]\s+(.+?)\s*[-–—]\s*https?://", line)
        if bullet:
            title = bullet.group(1).strip()
        elif re.match(r"^\s*[\*\-]\s+https?://", line):
            title = url
        add_link(result, url, title, rel)

    return result


def extract_all() -> list[LinkEntry]:
    result = ExtractResult()
    for path in sorted(GATECH.rglob("*.rst")):
        file_result = extract_from_file(path)
        for link in file_result.links:
            if link.url not in result.seen_urls:
                result.seen_urls.add(link.url)
                result.links.append(link)
    return result.links


def strip_external_links(text: str) -> str:
    """Remove external hyperlinks while preserving readable text."""

    # raw HTML blocks with external embeds
    text = RAW_HTML_BLOCK.sub("", text)

    # reference definitions pointing to external URLs
    text = RST_REF_DEF.sub("", text)

    # inline RST links with external URLs -> plain text
    text = RST_INLINE.sub(
        lambda m: m.group(1).strip() if m.group(2).startswith(("http://", "https://")) else m.group(0),
        text,
    )

    # markdown links -> text
    text = MARKDOWN_LINK.sub(r"\1", text)

    # external image directives
    text = IMAGE_EXT.sub("", text)

    # named references without targets become plain text
    text = RST_REF_USE.sub(r"\1", text)

    # bare URLs in lines — remove URL, keep preceding description
    lines = []
    for line in text.splitlines():
        if re.search(r"https?://", line):
            # bullet with description before URL
            m = re.match(r"^(\s*[\*\-]\s+.+?)\s*[-–—:]\s*https?://\S+\s*$", line)
            if m:
                lines.append(m.group(1))
                continue
            # bullet that is only a URL
            if re.match(r"^\s*[\*\-]\s+https?://\S+\s*$", line):
                continue
            # Reference:/Paper:/Resources: prefix
            m = re.match(r"^(\s*(?:Reference|Paper|Resources?):\s*).*$", line, re.I)
            if m and "http" in line:
                continue
            # parenthetical URL at end
            line = re.sub(r"\s*\(https?://[^)]+\)", "", line)
            # trailing bare URL after text
            line = re.sub(r"\s+https?://\S+", "", line)
            # line that is only a URL
            if re.match(r"^\s*https?://\S+\s*$", line):
                continue
        lines.append(line.rstrip())

    text = "\n".join(lines)

    # collapse excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    if not text.endswith("\n"):
        text += "\n"
    return text


def strip_all_files(dry_run: bool = False) -> list[str]:
    changed: list[str] = []
    for path in sorted(GATECH.rglob("*.rst")):
        original = path.read_text(encoding="utf-8", errors="replace")
        updated = strip_external_links(original)
        if updated != original:
            changed.append(str(path.relative_to(ROOT)))
            if not dry_run:
                path.write_text(updated, encoding="utf-8")
    return changed


def publish_to_linkding(links: Iterable[LinkEntry], api_key: str, dry_run: bool = False) -> dict:
    link_list = list(links)
    stats = {"created": 0, "skipped": 0, "errors": 0}
    for link in link_list:
        payload = {
            "url": link.url,
            "title": link.title[:512],
            "notes": f"Source: {link.source}\n{link.notes}".strip(),
            "tag_names": [TAG],
            "unread": False,
        }
        if dry_run:
            stats["created"] += 1
            continue
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            f"{LINKDING_BASE}/api/bookmarks/?disable_scraping=true",
            data=data,
            headers={
                "Authorization": f"Token {api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                if resp.status in (200, 201):
                    stats["created"] += 1
                    if stats["created"] % 25 == 0:
                        print(f"  ... {stats['created']}/{len(link_list)} published", flush=True)
                else:
                    stats["errors"] += 1
                    print(f"ERROR {resp.status}: {link.url}", file=sys.stderr)
        except urllib.error.HTTPError as e:
            stats["errors"] += 1
            body = e.read().decode("utf-8", errors="replace")
            print(f"HTTP {e.code} {link.url}: {body[:200]}", file=sys.stderr)
        except urllib.error.URLError as e:
            stats["errors"] += 1
            print(f"URL error {link.url}: {e}", file=sys.stderr)
        time.sleep(0.05)
    return stats


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Report only, no writes")
    parser.add_argument("--extract-only", action="store_true", help="Extract and list links")
    parser.add_argument("--strip-only", action="store_true", help="Strip docs without publishing")
    parser.add_argument("--publish-only", action="store_true", help="Publish from manifest without stripping")
    parser.add_argument("--manifest", type=Path, default=ROOT / "scripts" / "gatech_links_manifest.json")
    args = parser.parse_args()

    api_key = os.environ.get("LINKDING_API_KEY")
    if not api_key and not args.extract_only and not args.dry_run:
        print("LINKDING_API_KEY not set. Source env.sh first.", file=sys.stderr)
        return 1

    links = extract_all()
    print(f"Found {len(links)} unique external URLs in gatech/")

    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest = [
        {"url": l.url, "title": l.title, "source": l.source, "notes": l.notes}
        for l in links
    ]
    args.manifest.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote manifest: {args.manifest.relative_to(ROOT)}")

    if args.extract_only:
        for link in links:
            print(f"  [{link.source}] {link.title} -> {link.url}")
        return 0

    if not args.strip_only:
        print("Publishing to Linkding...")
        stats = publish_to_linkding(links, api_key or "", dry_run=args.dry_run)
        print(f"Linkding: {stats['created']} ok, {stats['errors']} errors")

    if not args.publish_only:
        print("Stripping external links from gatech/...")
        changed = strip_all_files(dry_run=args.dry_run)
        print(f"{'Would update' if args.dry_run else 'Updated'} {len(changed)} files")
        for f in changed:
            print(f"  {f}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
