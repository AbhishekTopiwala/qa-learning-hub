#!/bin/bash

# Script to update all HTML files to use header/footer components
# This makes the codebase more maintainable

echo "🔄 Updating HTML files to use component system..."

# List of files to update (excluding index.html which is already done)
FILES=(
  "manual-testing.html"
  "api-testing.html"
  "automation.html"
  "roadmap.html"
  "practice.html"
  "interview.html"
  "resume.html"
  "about.html"
  "bug-library.html"
)

for file in "${FILES[@]}"; do
  if [ -f "$file" ]; then
    echo "📝 Processing $file..."
    
    # Create backup
    cp "$file" "$file.backup"
    
    # Use Python to do the replacement more reliably
    python3 << 'PYTHON_SCRIPT'
import re
import sys

filename = sys.argv[1]

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace header section with placeholder
header_pattern = r'<header class="header">.*?</header>'
content = re.sub(header_pattern, '<!-- Header Placeholder (loaded from includes/header.html) -->\n    <div id="header-placeholder"></div>', content, flags=re.DOTALL)

# Replace footer section with placeholder
footer_pattern = r'<footer class="footer">.*?</footer>'
content = re.sub(footer_pattern, '<!-- Footer Placeholder (loaded from includes/footer.html) -->\n    <div id="footer-placeholder"></div>', content, flags=re.DOTALL)

# Add components.js if not already present
if 'components.js' not in content:
    content = re.sub(
        r'(<script src="js/main\.js"></script>)',
        r'<script src="js/components.js"></script>\n    \1',
        content
    )

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ Updated {filename}")

PYTHON_SCRIPT
"$file"
    
  else
    echo "⚠️  File not found: $file"
  fi
done

echo ""
echo "✨ Component system update complete!"
echo ""
echo "📊 Summary:"
echo "  - Header & Footer are now in includes/ folder"
echo "  - All pages load them dynamically"
echo "  - To update navigation, edit includes/header.html"
echo "  - To update footer, edit includes/footer.html"
