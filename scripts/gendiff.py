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
        choices=['plain', 'json'],
        default='plain'
    )

    args = parser.parse_args()
    # Дополнительные действия, которые вы хотите выполнить при использовании скрипта
    print(f'Comparing files: {args.first_file} and {args.second_file}')
    print(f'Selected format: {args.format}')

if __name__ == '__main__':
    main()

