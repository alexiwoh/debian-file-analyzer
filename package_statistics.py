#!/usr/bin/env python3

"""
Main entry point for the Debian File Analyzer CLI tool.

This script accepts a Debian architecture as a command-line argument, downloads the
corresponding Contents file from the Debian mirror, parses it, and prints
the top 10 packages with the highest number of associated files.
"""

import argparse

from utils import parse_contents


def main():
    """
    Parses command-line arguments and runs the package statistics analysis.

    The argument `architecture` should be a valid Debian architecture name,
    such as 'amd64', 'arm64', 'mipsel', etc.
    """
    parser = argparse.ArgumentParser(
        description="Analyzes Debian package file statistics from Contents index."
    )
    parser.add_argument(
        "architecture",
        type=str,
        help="Debian architecture to analyze (e.g., amd64, arm64, mipsel)",
    )
    args = parser.parse_args()

    try:
        contents = parse_contents(args.architecture)
    except Exception as e:
        print(f"Error parsing contents: {e}")
        return

    # Sort packages by file count in descending order and get the top 10
    sorted_packages = sorted(contents.items(), key=lambda item: item[1], reverse=True)
    top_packages = sorted_packages[:10]

    for i, (package, count) in enumerate(top_packages, start=1):
        print(f"{i}. {package}: {count}")


if __name__ == "__main__":
    main()
