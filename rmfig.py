#!/usr/bin/python3

import argparse

import fileutil


def remove_fig(filename, dryrun):
    fileutil.rename_numbered_files(filename, False, dryrun)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file_to_remove")
    parser.add_argument('--dry_run', action="store_true")
    args = parser.parse_args()
    remove_fig(args.file_to_remove, args.dry_run)
