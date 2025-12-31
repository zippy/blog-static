#!/usr/bin/env python3
"""
Convert posts with images to page bundles with thumbnails.
"""

import os
import re
import shutil
from pathlib import Path

POSTS_DIR = Path("/home/eric/code/blogs/eric/blog-static/content/posts")
STATIC_IMAGES = Path("/home/eric/code/blogs/eric/blog-static/static/images")

def find_first_image(content):
    """Find the first image reference in markdown content."""
    # Match markdown images: ![alt](/blog/images/file.jpg) or ![alt](images/file.jpg)
    md_pattern = r'!\[[^\]]*\]\((/blog/images/|/images/)([^)]+)\)'
    match = re.search(md_pattern, content)
    if match:
        return match.group(2)

    # Match HTML img tags: <img src="/blog/images/file.jpg" or src="/images/file.jpg"
    html_pattern = r'<img[^>]+src=["\'](?:/blog/images/|/images/)([^"\']+)["\']'
    match = re.search(html_pattern, content)
    if match:
        return match.group(1)

    return None

def convert_to_page_bundle(md_file):
    """Convert a single markdown file to a page bundle with thumbnail."""
    content = md_file.read_text()

    # Find first image
    image_name = find_first_image(content)
    if not image_name:
        return False, "No image found"

    # Check if source image exists
    source_image = STATIC_IMAGES / image_name
    if not source_image.exists():
        return False, f"Image not found: {image_name}"

    # Create directory for page bundle
    bundle_dir = md_file.parent / md_file.stem
    bundle_dir.mkdir(exist_ok=True)

    # Determine thumbnail extension
    ext = source_image.suffix.lower()
    if ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
        thumb_name = f"thumb{ext}"
    else:
        thumb_name = "thumb.jpg"

    # Copy image as thumbnail
    thumb_dest = bundle_dir / thumb_name
    shutil.copy2(source_image, thumb_dest)

    # Move markdown to index.md
    index_file = bundle_dir / "index.md"
    shutil.move(md_file, index_file)

    return True, f"Created bundle with {thumb_name}"

def main():
    converted = 0
    skipped = 0

    # Get all markdown files (not in subdirectories)
    md_files = [f for f in POSTS_DIR.glob("*.md") if f.is_file()]

    print(f"Found {len(md_files)} markdown files to process")

    for md_file in sorted(md_files):
        success, message = convert_to_page_bundle(md_file)
        if success:
            print(f"[OK] {md_file.name}: {message}")
            converted += 1
        else:
            print(f"[SKIP] {md_file.name}: {message}")
            skipped += 1

    print(f"\nDone: {converted} converted, {skipped} skipped")

if __name__ == "__main__":
    main()
