import gzip
from collections import defaultdict
from io import BytesIO

import requests

# Base URL for the Debian repository Contents indices
DEBIAN_BASE_URL = "http://ftp.uk.debian.org/debian/dists/stable/main"


def build_url(architecture: str) -> str:
    """
    Constructs the URL for the Contents index file based on architecture.

    Args:
        architecture (str): The target Debian architecture (e.g., 'amd64', 'arm64').

    Returns:
        str: Full URL to the Contents-<architecture>.gz file.
    """
    return f"{DEBIAN_BASE_URL}/Contents-{architecture}.gz"


def download_contents_file(url: str) -> bytes:
    """
    Downloads the gzip-compressed Contents file from the given URL.

    Args:
        url (str): URL to the .gz Contents file.

    Returns:
        bytes: Raw bytes of the downloaded gzip file.

    Raises:
        requests.HTTPError: If the download fails or returns an error status.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.content


def decompress_contents_file_gz(data: bytes) -> str:
    """
    Decompresses a .gz file and returns its contents as a UTF-8 string.

    Args:
        data (bytes): Gzip-compressed file content.

    Returns:
        str: Decompressed file content as a string.
    """
    with gzip.open(BytesIO(data), mode="rt", encoding="utf-8", errors="ignore") as f:
        return f.read()


def parse_contents_text(contents_text: str) -> dict:
    """
    Parses the decompressed Contents text and builds a dictionary of package to file count.

    Args:
        contents_text (str): Decompressed text of the Contents file.

    Returns:
        dict: Mapping of package names to the number of files associated with them.
    """
    package_counts = defaultdict(int)

    for line in contents_text.splitlines():
        if not line.strip() or line.startswith("FILE"):
            continue  # Skip the empty lines and headers

        try:
            # Split the line into path and package list (split on whitespace)
            path, packages = line.rsplit(None, 1)
            for pkg in packages.split(","):
                package_counts[pkg] += 1
        except ValueError:
            # Skip if the line cannot be parsed
            continue

    return dict(package_counts)


def parse_contents(architecture: str) -> dict:
    """
    Orchestrates the full parsing process: builds URL, downloads, decompresses, and parses.

    Args:
        architecture (str): The target Debian architecture (e.g., 'amd64', 'arm64').

    Returns:
        dict: Mapping of package names to file counts.

    Raises:
        Exception: If download or parsing fails at any stage.
    """
    url = build_url(architecture)
    print(f"⬇️Downloading from: {url}")
    raw_data = download_contents_file(url)
    text_data = decompress_contents_file_gz(raw_data)
    return parse_contents_text(text_data)
