# coding: utf-8
# Author: Mario Lenz <m@riolenz.de>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Ansible Project, 2022
"""The ansible-community CLI program."""

import argparse


def main():
    '''Main entrypoint for the ansible-community CLI program.'''
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--version',
        action='version',
        version='Ansible community version 7.7.0',
        help="show the version of the Ansible community package",
    )
    parser.parse_args()
    parser.print_help()


if __name__ == '__main__':
    main()
