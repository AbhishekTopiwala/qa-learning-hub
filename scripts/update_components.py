#!/usr/bin/env python3
"""
Script to update all HTML files to use the component system
Makes header and footer reusable across all pages
"""

import re
import os
from pathlib import Path

# Files to update
FILES = [
    "manual-testing.html",
    "api-testing.html",
    "automation.html",
    "roadmap.html",
    "practice.html",
    "interview.html",
    "resume.html",
    "about.html",
    "bug-library.html"
]

def update_file(filename):
    """Update a single HTML file to use components"""
    if not os.path.exists(filename):
        print(f"⚠️  File not found: {filename}")
        return
    
    print(f"📝 Processing {filename}...")
    
    # Read the file
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create backup
    with open(f"{filename}.backup", 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Replace header section with placeholder
    header_pattern = r'(\s*)<!-- Header & Navigation -->.*?</header>'
    header_replacement = r'\1<!-- Header Placeholder (loaded from includes/header.html) -->\n\1<div id="header-placeholder"></div>'
    content = re.sub(header_pattern, header_replacement, content, flags=re.DOTALL)
    
    # Replace footer section with placeholder
    footer_pattern = r'(\s*)<!-- Footer -->.*?</footer>'
    footer_replacement = r'\1<!-- Footer Placeholder (loaded from includes/footer.html) -->\n\1<div id="footer-placeholder"></div>'
    content = re.sub(footer_pattern, footer_replacement, content, flags=re.DOTALL)
    
    # Add components.js if not already present
    if 'components.js' not in content:
        content = re.sub(
            r'(\s*)<script src="js/main\.js"></script>',
            r'\1<script src="js/components.js"></script>\n\1<script src="js/main.js"></script>',
            content
        )
    
    # Write the updated content
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Updated {filename}")

def main():
    print("🔄 Updating HTML files to use component system...\n")
    
    for filename in FILES:
        update_file(filename)
    
    print("\n✨ Component system update complete!\n")
    print("📊 Summary:")
    print("  - Header & Footer are now in includes/ folder")
    print("  - All pages load them dynamically")
    print("  - To update navigation, edit includes/header.html")
    print("  - To update footer, edit includes/footer.html")
    print("\n💾 Backups created with .backup extension")

if __name__ == "__main__":
    main()
