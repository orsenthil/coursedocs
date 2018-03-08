"""
Converts an .srt file to rst file.

# Used with AI4R class transcripts.
"""

import glob
import sys

_LANGUAGE_FORMAT = "_en"


def _simply_numeric(line):
    try:
        int(line.strip())
    except ValueError:
        return False
    return True


def _contains_timestamp(line):
    return " --> " in line


def _empty_line(line):
    return len(line.strip()) == 0


def process_file(filename):
    with open(filename) as fh:
        raw_contents = fh.readlines()

    processed_contents = []
    for line in raw_contents:
        if not _simply_numeric(line) and not _contains_timestamp(line) and not _empty_line(line):
            processed_contents.append(line)
    formatted_contents = "".join(processed_contents)
    return formatted_contents


def sort_names(glob_list):
    return sorted(glob_list, key=lambda name: int(name.split("/")[-1].split(" - ")[0].strip()))


def translate_srt_to_rst(_directory_with_transcripts, _output_file):
    sorted_file_names = sort_names(glob.glob(_directory_with_transcripts + '/*.*'))
    with open(_output_file, 'w') as fhandle_output:
        for _glob_file in sorted_file_names:
            if _LANGUAGE_FORMAT in _glob_file:
                title = _glob_file.split("/")[-1].split(".")[0].rsplit("-", 1)[0]
                contents = process_file(_glob_file)
                fhandle_output.write(title)
                fhandle_output.write("\r\n")
                fhandle_output.write("=" * (len(title) - 1))
                fhandle_output.write("\r\n")
                fhandle_output.write(contents)
                fhandle_output.write("\r\n")


if __name__ == '__main__':
    _directory_with_transcripts = sys.argv[1]
    _output_file = '/Users/senthil/gatech/air4/output.rst'
    translate_srt_to_rst(_directory_with_transcripts, _output_file)
