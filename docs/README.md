# Ubuntu Image Fetcher - User Guide

## Quick Start

1. Run `python ubuntu_fetcher.py`
2. Choose option 1 for single image or option 2 for multiple images
3. Enter the image URL(s)
4. Images will be saved to the `Fetched_Images` folder

## Safety Features

The fetcher includes several safety measures:

- **Content validation**: Checks if URLs actually point to images
- **Size warnings**: Alerts you to large files before downloading
- **Duplicate detection**: Prevents downloading the same image twice
- **Timeout protection**: Won't hang on slow connections

## Supported Image Formats

- JPEG/JPG
- PNG
- GIF
- WebP
- BMP
- SVG

## Error Handling

The program gracefully handles:
- Network connection issues
- Invalid URLs
- Server errors (404, 500, etc.)
- Timeout errors
- File system errors

## Ubuntu Philosophy

This tool embodies Ubuntu principles:
- **Community**: Respectful interaction with web servers
- **Sharing**: Easy organization for sharing downloaded images
- **Respect**: Graceful error handling without disruption
- **Practicality**: Solves real needs for image collection
