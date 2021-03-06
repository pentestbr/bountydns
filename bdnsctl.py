#!/usr/bin/env python

from sys import exit
from bountydns.core.utils import load_env

load_env("core")

from bountydns.cli import make_parser, commands

if __name__ == "__main__":
    parser = make_parser()
    args = parser.parse_args()
    for command in commands:
        if command.has_command(args.command):
            exit(command.make(args).run())
    parser.print_help()
    exit(1)
