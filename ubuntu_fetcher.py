import requests
import os
import hashlib
from urllib.parse import urlparse
from pathlib import Path

def get_file_hash(filepath):
    """Generate MD5 hash of a file to check for duplicates."""
    hash_md5 = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def is_safe_content_type(content_type):
    """Check if the content type is a safe image format."""
    safe_types = [
        'image/jpeg', 'image/jpg', 'image/png', 'image/gif', 
        'image/webp', 'image/bmp', 'image/svg+xml'
    ]
    return any(safe_type in content_type.lower() for safe_type in safe_types)

def get_filename_from_url(url, content_type=None):
    """Extract filename from URL or generate one based on content type."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    
    if not filename or '.' not in filename:
        # Generate filename based on content type
        if content_type:
            if 'jpeg' in content_type or 'jpg' in content_type:
                extension = '.jpg'
            elif 'png' in content_type:
                extension = '.png'
            elif 'gif' in content_type:
                extension = '.gif'
            elif 'webp' in content_type:
                extension = '.webp'
            else:
                extension = '.jpg'  # Default
        else:
            extension = '.jpg'
        
        filename = f"downloaded_image_{hash(url) % 10000}{extension}"
    
    return filename

def download_image(url, directory="Fetched_Images"):
    """Download a single image from URL."""
    try:
        print(f"Fetching: {url}")
        
        # Make request with headers to appear more legitimate
        headers = {
            'User-Agent': 'Mozilla/5.0 (Ubuntu; Linux x86_64) AppleWebKit/537.36'
        }
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()
        
        # Check content type for safety
        content_type = response.headers.get('content-type', '')
        if not is_safe_content_type(content_type):
            print(f"  Warning: Content type '{content_type}' may not be an image")
            proceed = input("Continue anyway? (y/N): ").lower().strip()
            if proceed != 'y':
                print(" Download cancelled")
                return False
        
        # Check content length
        content_length = response.headers.get('content-length')
        if content_length:
            size_mb = int(content_length) / (1024 * 1024)
            if size_mb > 50:  # 50MB limit
                print(f"  Large file detected: {size_mb:.1f}MB")
                proceed = input("Continue download? (y/N): ").lower().strip()
                if proceed != 'y':
                    print(" Download cancelled")
                    return False
        
        # Get filename
        filename = get_filename_from_url(url, content_type)
        filepath = os.path.join(directory, filename)
        
        # Check for duplicates
        if os.path.exists(filepath):
            print(f" File already exists: {filename}")
            # Check if it's actually the same file
            temp_path = filepath + ".temp"
            with open(temp_path, 'wb') as f:
                f.write(response.content)
            
            if get_file_hash(temp_path) == get_file_hash(filepath):
                os.remove(temp_path)
                print("✓ Identical file already exists, skipping")
                return True
            else:
                # Different file, rename
                base, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(filepath):
                    filename = f"{base}_{counter}{ext}"
                    filepath = os.path.join(directory, filename)
                    counter += 1
                os.rename(temp_path, filepath)
        else:
            # Save the image
            with open(filepath, 'wb') as f:
                f.write(response.content)
        
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        return True
        
    except requests.exceptions.Timeout:
        print(" Connection timeout - the server took too long to respond")
        return False
    except requests.exceptions.ConnectionError:
        print(" Connection error - unable to reach the server")
        return False
    except requests.exceptions.HTTPError as e:
        print(f" HTTP error: {e}")
        return False
    except requests.exceptions.RequestException as e:
        print(f" Request error: {e}")
        return False
    except Exception as e:
        print(f" An unexpected error occurred: {e}")
        return False

def main():
    print(" Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web")
    print("Ubuntu wisdom: 'I am because we are'\n")
    
    # Create directory if it doesn't exist
    directory = "Fetched_Images"
    os.makedirs(directory, exist_ok=True)
    print(f" Directory ready: {directory}\n")
    
    while True:
        print("\nOptions:")
        print("1. Download single image")
        print("2. Download multiple images")
        print("3. Exit")
        
        choice = input("\nSelect an option (1-3): ").strip()
        
        if choice == '1':
            url = input("\nPlease enter the image URL: ").strip()
            if url:
                success = download_image(url, directory)
                if success:
                    print("\n Connection strengthened. Community enriched.")
            else:
                print(" Please enter a valid URL")
                
        elif choice == '2':
            print("\nEnter image URLs (one per line, empty line to finish):")
            urls = []
            while True:
                url = input().strip()
                if not url:
                    break
                urls.append(url)
            
            if urls:
                successful = 0
                total = len(urls)
                print(f"\n Processing {total} URLs...")
                
                for i, url in enumerate(urls, 1):
                    print(f"\n[{i}/{total}]")
                    if download_image(url, directory):
                        successful += 1
                
                print(f"\n Summary: {successful}/{total} images downloaded successfully")
                if successful > 0:
                    print("Connections strengthened. Community enriched.")
            else:
                print(" No URLs provided")
                
        elif choice == '3':
            print("\n Thank you for using Ubuntu Image Fetcher!")
            print("May your connections remain strong. Ubuntu! 🌍")
            break
            
        else:
            print(" Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
