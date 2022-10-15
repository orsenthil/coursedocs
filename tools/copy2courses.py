#!/usr/bin/env python3

import sys
import glob
import os
import subprocess

SCREENSHOTS_DIR = '/Users/senthilx/git/notes/source/_static'
COURSEDOCS_DIR = '/Users/senthilx/git/coursedocs/_static'


def get_latest_file():
    list_of_files = glob.glob(SCREENSHOTS_DIR + '/*')
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file


def copy_screenshot(filename=None):
    if filename is not None:
        destination = os.path.join(COURSEDOCS_DIR, filename)
    else:
        destination = COURSEDOCS_DIR

    destination_filename = destination.split('/')[-1]

    latest_file = get_latest_file()

    subprocess.run(['cp', latest_file, destination])

    subprocess.run(['open', destination])

    print(f'Copied {latest_file} to {destination_filename}')

    return destination_filename


if __name__ == '__main__':
    optional_file_name = None
    if len(sys.argv) == 2:
        optional_file_name = sys.argv[1]

    destination_filename = copy_screenshot(optional_file_name)

    subprocess.run(['pbcopy', destination_filename])
