#!/usr/bin/env python

import argparse

def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='First file')
    parser.add_argument('second_file', help='Second file')
    parser.add_argument(
        '-f', '--format',
        help='Set format of output',
        metavar='FORMAT',
        choices=['plain', 'json'],
        default='plain'
    )

    args = parser.parse_args()

if __name__ == '__main__':
    main()

