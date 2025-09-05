# Ubuntu Image Fetcher 

*"I am because we are"* - Ubuntu Philosophy

A Python tool for mindfully collecting images from the web, built with the Ubuntu principles of community, respect, sharing, and practicality.

## Features

- **Single & Batch Downloads**: Download one image or multiple images at once
- **Smart Duplicate Detection**: Prevents downloading identical files using MD5 hashing
- **Safety Checks**: Validates content types and file sizes before downloading
- **Error Handling**: Graceful handling of network issues and invalid URLs
- **Ubuntu Philosophy**: Built with respect for the global web community

## Installation

1. Clone this repository:
\`\`\`bash
git clone https://github.com/Suudi-sudo/Ubuntu_Requests.git
cd Ubuntu_Requests
\`\`\`

2. Install dependencies:
\`\`\`bash
pip install -r pipfile
\`\`\`

## Usage

Run the script:
\`\`\`bash
python ubuntu_fetcher.py
\`\`\`

The program will guide you through:
1. **Single Image Download**: Enter one URL to download
2. **Multiple Image Download**: Enter multiple URLs (one per line)
3. **Exit**: Close the program

### Example
\`\`\`
 Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web
Ubuntu wisdom: 'I am because we are'

 Directory ready: Fetched_Images

Please enter the image URL: https://example.com/ubuntu-wallpaper.jpg
 Fetching: https://example.com/ubuntu-wallpaper.jpg
✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg

 Connection strengthened. Community enriched.
\`\`\`

## Safety Features

- **Content Type Validation**: Checks if the URL actually points to an image
- **File Size Limits**: Warns about large files (>50MB) before downloading
- **Duplicate Prevention**: Uses MD5 hashing to avoid downloading identical files
- **Timeout Protection**: Prevents hanging on slow connections
- **User Agent Headers**: Respectful requests that identify as Ubuntu-based

## Project Structure

\`\`\`
Ubuntu_Requests/
├── README.md                # This file
├── ubuntu_fetcher.py        # Main Python script
├── pipfile         # Dependencies
├── docs/
│   └── README.md           # Additional documentation
├── Fetched_Images/         # Downloaded images folder
└── .gitignore             # Git ignore file
\`\`\`

## Ubuntu Principles Implemented

- **Community**: Connects respectfully to the global web
- **Respect**: Handles errors gracefully without disruption
- **Sharing**: Organizes images for easy sharing and access
- **Practicality**: Provides real utility for image collection

## Challenge Features Implemented

 **Multiple URLs**: Batch download functionality  
 **Safety Precautions**: Content type and size validation  
 **Duplicate Prevention**: MD5 hash-based duplicate detection  
 **HTTP Headers**: Content-Type and Content-Length checking  

## Contributing

Feel free to contribute improvements that align with Ubuntu principles of community and respect.

## License

This project embodies the spirit of Ubuntu - free and open for all to use and improve.
