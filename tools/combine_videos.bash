#!/usr/bin/env bash

find -name "* *" -type f | rename 's/ /_/g'
find -name "*,*" -type f | rename 's/,/_/g'
find -name "*-*" -type f | rename 's/-/_/g'
find -name "*:*" -type f | rename 's/:/_/g'
find -name "*\?*" -type f | rename 's/\?/_/g'
find -name "*\)*" -type f | rename 's/\)/_/g'
find -name "*\(*" -type f | rename 's/\(/_/g'

ls -1v | grep -v "^output-list.txt$" > output-list.txt
sed -i 's/^/file /' output-list.txt

ffmpeg -f concat -i output-list.txt -c copy output.mp4
