**URL Slug Extractor**
=====================

A simple Python script to extract meaningful slugs from URLs.

## Table of Contents

* [Overview](#overview)
* [Usage](#usage)
* [Features](#features)
* [Requirements](#requirements)
* [Installation](#installation)
* [Contributing](#contributing)
* [License](#license)
* [Known Issues](#known-issues)


## Overview

This script takes a list of URLs as input and returns a list of corresponding slugs. The slug is extracted by removing the `.html` extension, handling empty sections after the final slash, and extracting segments before subsequent slashes.

## Usage

To use this script, simply run the `URLSlugExtractor.py` file and follow the prompts:

* Enter URLs separated by newlines (or press Enter on an empty line to finish)
* The script will generate slugs for each URL and print them to the console

## Features

* Removes `.html` extension from URLs
* Handles empty sections after final slash
* Extracts segments before subsequent slashes
* Replaces hyphens with spaces and converts to lowercase
* Strips whitespace from generated slugs

## Requirements

* Python 3.x (tested on Python 3.8 and later)

## Installation

1. Clone the repository: `git clone https://github.com/harshuqt/url-slug-extractor.git`
2. Navigate to the project directory: `cd url-slug-extractor`
3. Run the script: `python URLSlugExtractor.py`

## Contributing

Pull requests are welcome! If you'd like to contribute to this project, please submit a pull request with your changes.

## License

This project is licensed under the [GNU General Public License v3.0](https://github.com/Harshuqt/URL-Slug-Extractor/blob/main/LICENSE). See the LICENSE file in this repository for details.

## Known Issues

* No known issues at this time. However, if you encounter any bugs or issues, please report them in the issue tracker.

## Future Development

* Add support for non-HTTP URLs (e.g., FTP, SSH)
* Provide an option to preserve URL query parameters or fragment identifiers
* Allow users to customize the slug generation process
