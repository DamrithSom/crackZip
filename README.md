# Zip File Cracker

![Version](https://img.shields.io/badge/version-1.0-brightgreen)

## Description

A simple Python script for cracking password-protected zip files using a wordlist. This script leverages the `zipfile` module to attempt to extract files from a zip archive using passwords listed in a text file.

## Features

- User-friendly GUI for file selection.
- Attempts to crack zip passwords using a specified password list.
- Displays success and failure messages for each password attempt.
- Easy to run with minimal dependencies.

## Prerequisites

- Python 3.x
- Required libraries:
  - `colorama`
  - `tkinter` (usually included with Python)
  
You can install the required library using pip:

```bash
pip install colorama
