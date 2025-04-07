"""
Unit tests for the Debian File Analyzer utility functions.

Tests cover URL construction and parsing of Contents file lines into
a package → file count mapping.
"""

import unittest

from utils import build_url, parse_contents_text


class TestUtils(unittest.TestCase):
    """
    Unit tests for helper functions in utils.py.
    """

    def test_build_url(self):
        """
        Verifies that the URL is correctly constructed for a given architecture.
        """
        arch = "amd64"
        expected_url = (
            "http://ftp.uk.debian.org/debian/dists/stable/main/Contents-amd64.gz"
        )
        self.assertEqual(build_url(arch), expected_url)

    def test_parse_contents_text_basic(self):
        """
        Tests parsing a simple Contents file input with single-package entries.
        """
        mock_text = """
FILE                    LOCATION
usr/bin/python3         python3
usr/bin/pip3            python3-pip
usr/share/doc/bash/README    bash
"""
        expected = {"python3": 1, "python3-pip": 1, "bash": 1}
        result = parse_contents_text(mock_text)
        self.assertEqual(result, expected)

    def test_parse_contents_text_with_multiple_packages(self):
        """
        Tests that the parser can handle lines where multiple packages share a file.
        """
        mock_text = """
usr/share/doc/common/LICENSE    coreutils,base-files
"""
        expected = {"coreutils": 1, "base-files": 1}
        result = parse_contents_text(mock_text)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
