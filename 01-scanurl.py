import os
import re
import zipfile
import requests
from pathlib import Path
import time

# Regular expression to detect URLs
URL_REGEX = re.compile(r'https?://[^\s"\'>]+')

# File extensions to analyze
TEXT_EXTENSIONS = {'.txt'}


def extract_urls_from_file(filepath):
    """Reads a text file and extracts URLs."""
    urls = set()
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            urls.update(URL_REGEX.findall(content))
            print(f"FILE : Extracting URL from {filepath}")
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return urls


def extract_urls_from_zip(zip_path):
    """Extracts URLs from .txt files inside a ZIP archive."""
    urls = set()
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            for file_info in zip_ref.infolist():
                if any(file_info.filename.endswith(ext) for ext in TEXT_EXTENSIONS):
                    try:
                        with zip_ref.open(file_info) as file:
                            content = file.read().decode('utf-8', errors='ignore')
                            urls.update(URL_REGEX.findall(content))
                            print(f"ZIP opening zip file : {zip_path}")
                    except Exception as e:
                        print(f"Error in ZIP {zip_path}, file {file_info.filename}: {e}")
    except Exception as e:
        print(f"Error opening ZIP {zip_path}: {e}")
    return urls


def scan_directory(root_dir):
    """Walks through the directory tree and collects all URLs."""
    all_urls = set()
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            ext = os.path.splitext(filename)[1].lower()
            if ext in TEXT_EXTENSIONS:
                all_urls.update(extract_urls_from_file(filepath))
            elif ext == '.zip':
                all_urls.update(extract_urls_from_zip(filepath))
    return all_urls


def write_urls_to_file(urls, output_path):
    """Writes extracted URLs to a text file."""
    with open(output_path, 'w', encoding='utf-8') as file:
        for url in sorted(urls):
            file.write(url + '\n')

if __name__ == '__main__':
    # Define input and output paths
    input_directory = Path(r"S:\saves\palm\palmtops CD\extractionURL") # Put the folder structure to be scanned here
    output_urls_file = Path(r"S:\saves\palm\palmtops CD\palmtops_url.txt") # outputs all developer homepage URL

    print(f"Scanning directory: {input_directory}")
    found_urls = scan_directory(str(input_directory))
    write_urls_to_file(found_urls, str(output_urls_file))
    print(f"{len(found_urls)} URL(s) found. Results written to '{output_urls_file}'")
