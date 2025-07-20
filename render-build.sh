#!/usr/bin/env bash

# Update and install Tesseract
apt-get update && apt-get install -y tesseract-ocr

# Continue with the Python environment
pip install -r requirements.txt
