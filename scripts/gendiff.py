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

import json


def generate_diff(file_path1, file_path2):
    data1 = load_data(file_path1)
    data2 = load_data(file_path2)
    diff = find_differences(data1, data2)
    return format_diff(diff)


def load_data(file_path):
    with open(file_path) as file:
        return json.load(file)


def find_differences(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []
    for key in keys:
        if key not in data1:
            diff.append(create_added_line(key, data2[key]))
        elif key not in data2:
            diff.append(create_removed_line(key, data1[key]))
        elif data1[key] != data2[key]:
            diff.append(create_changed_line(key, data1[key], data2[key]))
        else:
            diff.append(create_unchanged_line(key, data1[key]))
    return diff


def create_added_line(key, value):
    return f"  + {key}: {format_value(value)}"


def create_removed_line(key, value):
    return f"  - {key}: {format_value(value)}"


def create_changed_line(key, value1, value2):
    return f"  - {key}: {format_value(value1)}\n  + {key}: {format_value(value2)}"


def create_unchanged_line(key, value):
    return f"    {key}: {format_value(value)}"


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def format_diff(diff):
    return "{\n" + "\n".join(diff) + "\n}"
