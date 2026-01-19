#!/usr/bin/env python3
"""
Update file paths after folder reorganization
"""

import os
import re
from pathlib import Path

def update_paths_in_file(filepath, path_updates):
    """Update all paths in a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply all path updates
        for old_path, new_path in path_updates.items():
            content = content.replace(old_path, new_path)
        
        # Only write if content changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error updating {filepath}: {e}")
        return False

def main():
    print("🔄 Updating file paths after reorganization...\n")
    
    # Define path mappings based on file location
    learn_pages_updates = {
        'href="css/': 'href="../../css/',
        'src="js/': 'src="../../js/',
        'href="favicon.png"': 'href="../../favicon.png"',
        'href="includes/header.html"': 'href="../../includes/header.html"',
        'href="includes/footer.html"': 'href="../../includes/footer.html"',
        
        # Update navigation links
        'href="index.html"': 'href="../../index.html"',
        'href="roadmap.html"': 'href="../../pages/roadmap.html"',
        'href="manual-testing.html"': 'href="manual-testing.html"',
        'href="automation.html"': 'href="automation.html"',
        'href="api-testing.html"': 'href="api-testing.html"',
        'href="practice.html"': 'href="../tools/practice.html"',
        'href="interview.html"': 'href="../tools/interview.html"',
        'href="resume.html"': 'href="../tools/resume.html"',
        'href="about.html"': 'href="../../pages/about.html"',
    }
    
    tools_pages_updates = {
        'href="css/': 'href="../../css/',
        'src="js/': 'src="../../js/',
        'href="favicon.png"': 'href="../../favicon.png"',
        'href="includes/header.html"': 'href="../../includes/header.html"',
        'href="includes/footer.html"': 'href="../../includes/footer.html"',
        
        # Update navigation links
        'href="index.html"': 'href="../../index.html"',
        'href="roadmap.html"': 'href="../../pages/roadmap.html"',
        'href="manual-testing.html"': 'href="../learn/manual-testing.html"',
        'href="automation.html"': 'href="../learn/automation.html"',
        'href="api-testing.html"': 'href="../learn/api-testing.html"',
        'href="practice.html"': 'href="practice.html"',
        'href="interview.html"': 'href="interview.html"',
        'href="resume.html"': 'href="resume.html"',
        'href="bug-library.html"': 'href="bug-library.html"',
        'href="about.html"': 'href="../../pages/about.html"',
    }
    
    general_pages_updates = {
        'href="css/': 'href="../css/',
        'src="js/': 'src="../js/',
        'href="favicon.png"': 'href="../favicon.png"',
        'href="includes/header.html"': 'href="../includes/header.html"',
        'href="includes/footer.html"': 'href="../includes/footer.html"',
        
        # Update navigation links
        'href="index.html"': 'href="../index.html"',
        'href="roadmap.html"': 'href="roadmap.html"',
        'href="manual-testing.html"': 'href="learn/manual-testing.html"',
        'href="automation.html"': 'href="learn/automation.html"',
        'href="api-testing.html"': 'href="learn/api-testing.html"',
        'href="practice.html"': 'href="tools/practice.html"',
        'href="interview.html"': 'href="tools/interview.html"',
        'href="resume.html"': 'href="tools/resume.html"',
        'href="bug-library.html"': 'href="tools/bug-library.html"',
        'href="about.html"': 'href="about.html"',
    }
    
    # Update learn pages
    learn_dir = Path('pages/learn')
    if learn_dir.exists():
        for html_file in learn_dir.glob('*.html'):
            if update_paths_in_file(html_file, learn_pages_updates):
                print(f"✅ Updated {html_file}")
    
    # Update tools pages
    tools_dir = Path('pages/tools')
    if tools_dir.exists():
        for html_file in tools_dir.glob('*.html'):
            if update_paths_in_file(html_file, tools_pages_updates):
                print(f"✅ Updated {html_file}")
    
    # Update general pages
    pages_dir = Path('pages')
    for html_file in pages_dir.glob('*.html'):
        if update_paths_in_file(html_file, general_pages_updates):
            print(f"✅ Updated {html_file}")
    
    # Update header component
    header_updates = {
        'href="index.html"': 'href="../index.html"',
        'href="roadmap.html"': 'href="../pages/roadmap.html"',
        'href="manual-testing.html"': 'href="../pages/learn/manual-testing.html"',
        'href="automation.html"': 'href="../pages/learn/automation.html"',
        'href="api-testing.html"': 'href="../pages/learn/api-testing.html"',
        'href="practice.html"': 'href="../pages/tools/practice.html"',
        'href="interview.html"': 'href="../pages/tools/interview.html"',
        'href="resume.html"': 'href="../pages/tools/resume.html"',
        'href="about.html"': 'href="../pages/about.html"',
    }
    
    header_file = Path('includes/header.html')
    if header_file.exists():
        if update_paths_in_file(header_file, header_updates):
            print(f"✅ Updated {header_file}")
    
    # Update footer component  
    footer_updates = {
        'href="about.html"': 'href="../pages/about.html"',
        'href="roadmap.html"': 'href="../pages/roadmap.html"',
        'href="practice.html"': 'href="../pages/tools/practice.html"',
        'href="interview.html"': 'href="../pages/tools/interview.html"',
        'href="manual-testing.html"': 'href="../pages/learn/manual-testing.html"',
        'href="api-testing.html"': 'href="../pages/learn/api-testing.html"',
    }
    
    footer_file = Path('includes/footer.html')
    if footer_file.exists():
        if update_paths_in_file(footer_file, footer_updates):
            print(f"✅ Updated {footer_file}")
    
    print("\n✨ Path update complete!")

if __name__ == "__main__":
    main()
