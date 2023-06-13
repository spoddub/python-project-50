#!/usr/bin/env python

import argparse


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='First file')
    parser.add_argument('second_file', help='Second file')

    args = parser.parse_args()
    # Дополнительные действия, которые вы хотите выполнить при использовании скрипта


if __name__ == '__main__':
    main()
