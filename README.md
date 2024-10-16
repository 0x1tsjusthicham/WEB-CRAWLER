
# URL Crawler and Subdomain/File Finder

This repository contains a Python script that helps in discovering available subdomains, files, and links on a given target website. It is a simple tool that performs basic enumeration of subdomains and files from a wordlist, as well as a basic web crawler to extract links from a target page.

## Overview

### Features:
- **Subdomain Discovery**: Uses a wordlist to find available subdomains of the given target URL.
- **File Discovery**: Uses a wordlist to find available files and directories on the target URL.
- **Link Extraction**: Extracts all links from the HTML content of a target URL and crawls through them.

## Prerequisites

- Python 3.x
- Libraries: `requests`, `optparse`, `re`, `urllib`

## Usage

1. Clone this repository and navigate to the directory containing the script.

2. Make sure you have wordlist files named `Subdomain.txt` and `files.txt` in the same directory. These should contain a list of potential subdomains and files to test, each on a new line.

3. Run the script with the following command:

    ```bash
    python3 script.py -u <target_url>
    ```

    Replace `<target_url>` with the domain you want to target (e.g., `example.com`).

## Example

```bash
python3 script.py -u example.com
```

This command will:
- Attempt to discover subdomains of `example.com` using `Subdomain.txt`.
- Attempt to discover files and directories using `files.txt`.
- Extract and crawl links from the provided `example.com`.

## Disclaimer

This script is intended for educational purposes only. Unauthorized access to computer systems or networks is illegal and unethical. Always ensure you have explicit permission before using this script on any website or system.

# 0x1tsjusthicham
