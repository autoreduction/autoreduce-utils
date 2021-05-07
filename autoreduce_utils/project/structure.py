# ############################################################################### #
# Autoreduction Repository : https://github.com/ISISScientificComputing/autoreduce
#
# Copyright &copy; 2019 ISIS Rutherford Appleton Laboratory UKRI
# SPDX - License - Identifier: GPL-3.0-or-later
# ############################################################################### #
"""
Helper functions for navigating the project
"""

from pathlib import Path


def get_project_root() -> str:
    """
    Use git to find the project root
    :return: file path to root of the project folder
    """
    return str(Path("~/.autoreduce").expanduser())


PROJECT_ROOT = get_project_root()
