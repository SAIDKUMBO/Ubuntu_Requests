import requests
import os
from urllib.parse import urlparse

def fetch_image(url):
    """Fetch and save a single image from a given URL."""
    try:
        # Create Fetched_Images directory if not exists
        os.makedirs("Fetched_Images", exist_ok=True)

        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Confirm it's an image using Content-Type header
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped (not an image): {url}")
            return

        # Extract filename
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # Fallback filename if URL has no name
        if not filename or "." not in filename:
            ext = content_type.split("/")[-1] if "/" in content_type else "jpg"
            filename = f"downloaded_image.{ext}"

        filepath = os.path.join("Fetched_Images", filename)

        # Prevent duplicates
        base, ext = os.path.splitext(filepath)
        counter = 1
        while os.path.exists(filepath):
            filepath = f"{base}_{counter}{ext}"
            counter += 1

        # Save the image
        with open(filepath, "wb") as file:
            file.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    urls = input("Please enter one or more image URLs (separated by spaces): ").split()

    for url in urls:
        fetch_image(url)

    print("\nConnection strengthened. Community enriched.")


if __name__ == "__main__":
    main()
