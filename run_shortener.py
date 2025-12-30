# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from shortener.core import URLShortener

def main():
    parser = argparse.ArgumentParser(description="URL Shortener CLI (TinyURL)")
    parser.add_argument("url", help="The long URL to shorten")
    
    args = parser.parse_args()

    shortener = URLShortener()
    print("Shortening...")
    short_url = shortener.shorten(args.url)
    
    if short_url.startswith("Error"):
        print(short_url)
        sys.exit(1)
    else:
        print(f"Long URL : {args.url}")
        print(f"Short URL: {short_url}")

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
