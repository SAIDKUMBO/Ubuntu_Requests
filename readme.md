Ubuntu-Inspired Image Fetcher

"I am because we are." – Ubuntu Philosophy

This project is a simple but meaningful Python tool that embraces the wisdom of Ubuntu: connecting with the wider community, sharing resources, and respecting others.

The Ubuntu Image Fetcher allows you to download and organize images from the web into a local folder, handling errors gracefully and ensuring that your collection is always neat and respectful.

Features

Fetches one or multiple images from provided URLs

Automatically creates a Fetched_Images directory if it doesn’t exist

Extracts filenames from URLs (or generates one if missing)

Skips non-image files using Content-Type check

Prevents overwriting by renaming duplicate files (image.jpg → image_1.jpg)

Handles errors gracefully without crashing

Ubuntu Principles in the Program

Community → Connects to the global internet to fetch shared resources

Respect → Errors are handled mindfully without crashing

Sharing → Downloads are neatly stored for later sharing

Practicality → A real-world tool for organizing web images

Getting Started
1. Clone the Repository
git clone https://github.com/<your-username>/Ubuntu_Requests.git
cd Ubuntu_Requests

2. Install Requirements

This project uses the requests library:

pip install requests

3. Run the Program
python ubuntu_fetcher.py

Example Usage

Terminal Output:

Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter one or more image URLs (separated by spaces): 
https://example.com/ubuntu-wallpaper.jpg https://example.com/logo.png

✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg
✓ Successfully fetched: logo.png
✓ Image saved to Fetched_Images/logo.png

Connection strengthened. Community enriched.

Challenge Extensions

You can extend the program with:

Reading multiple URLs from a file

Adding extra precautions for unknown sources (file type checks, size limits)

Avoiding duplicate downloads by checking hashes

Verifying important HTTP headers before saving

License

This project is shared in the spirit of Ubuntu – feel free to use, learn, and improve it.

"A person is a person through other persons." – By using this program, you connect with the work of others across the web.
