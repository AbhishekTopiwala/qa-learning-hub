#!/usr/bin/env python3
"""
Premium Design Applicator - Updates all HTML pages with premium header/footer
"""

import os
from pathlib import Path

# Premium header HTML
HEADER_HTML = '''    <!-- Header & Navigation -->
    <header class="header">
        <nav class="container">
            <div class="nav">
                <a href="../index.html" class="logo">QA Learning Hub</a>

                <button class="hamburger" aria-label="Toggle menu">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>

                <ul class="nav-menu">
                    <li class="nav-item"><a href="../index.html" class="nav-link">Home</a></li>
                    <li class="nav-item"><a href="../pages/roadmap.html" class="nav-link">QA Roadmap</a></li>
                    <li class="nav-item dropdown">
                        <a href="#" class="nav-link">Learn</a>
                        <ul class="dropdown-menu">
                            <li class="dropdown-item"><a href="../pages/learn/manual-testing.html" class="dropdown-link">Manual Testing</a></li>
                            <li class="dropdown-item"><a href="../pages/learn/automation.html" class="dropdown-link">Automation Testing</a></li>
                            <li class="dropdown-item"><a href="../pages/learn/api-testing.html" class="dropdown-link">API Testing</a></li>
                        </ul>
                    </li>
                    <li class="nav-item"><a href="../pages/tools/practice.html" class="nav-link">Practice Zone</a></li>
                    <li class="nav-item"><a href="../pages/tools/interview.html" class="nav-link">Interview Prep</a></li>
                    <li class="nav-item"><a href="../pages/tools/resume.html" class="nav-link">Resume & Career</a></li>
                    <li class="nav-item"><a href="../pages/about.html" class="nav-link">About</a></li>
                </ul>
            </div>
        </nav>
    </header>
'''

# Premium footer HTML
FOOTER_HTML = '''    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <ul class="footer-links">
                <li><a href="../pages/about.html">About</a></li>
                <li><a href="../pages/roadmap.html">Roadmap</a></li>
                <li><a href="../pages/tools/practice.html">Practice</a></li>
                <li><a href="../pages/tools/interview.html">Interview</a></li>
                <li><a href="../pages/learn/manual-testing.html">Manual Testing</a></li>
                <li><a href="../pages/learn/api-testing.html">API Testing</a></li>
            </ul>
            <p class="footer-text">© 2026 QA Learning Hub. Built by QA professionals, for QA learners.</p>
        </div>
    </footer>
'''

# Deep pages header (for learn/ and tools/ subdirectories)
DEEP_HEADER_HTML = HEADER_HTML.replace('../index.html', '../../index.html').replace('../pages/', '../../pages/')

# Deep pages footer
DEEP_FOOTER_HTML = FOOTER_HTML.replace('../pages/', '../../pages/')

def update_html_file(file_path, is_deep=False):
    """Update an HTML file with premium header and footer"""
    
    print(f"Updating: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Choose appropriate header/footer based on depth
    header = DEEP_HEADER_HTML if is_deep else HEADER_HTML
    footer = DEEP_FOOTER_HTML if is_deep else FOOTER_HTML
    
    # Replace header placeholder or old header
    if '<div id="header-placeholder"></div>' in content:
        content = content.replace('<div id="header-placeholder"></div>', header)
    elif '<!-- Header Placeholder' in content:
        # Find and replace the placeholder comment section
        start = content.find('<!-- Header Placeholder')
        end = content.find('</div>', start) + 6
        if start != -1 and end != -1:
            content = content[:start] + header + '\n' + content[end:]
    
    # Replace footer placeholder or old footer
    if '<div id="footer-placeholder"></div>' in content:
        content = content.replace('<div id="footer-placeholder"></div>', footer)
    elif '<!-- Footer Placeholder' in content:
        start = content.find('<!-- Footer Placeholder')
        end = content.find('</div>', start) + 6
        if start != -1 and end != -1:
            content = content[:start] + footer + '\n' + content[end:]
    
    # Remove components.js script if present
    content = content.replace('<script src="js/components.js"></script>', '')
    content = content.replace('<script src="../js/components.js"></script>', '')
    content = content.replace('<script src="../../js/components.js"></script>', '')
    
    # Ensure loading class on body
    if '<body>' in content and 'class="loading"' not in content:
        content = content.replace('<body>', '<body class="loading">')
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Updated: {file_path}")

def main():
    base_dir = Path('/home/im0277/Desktop/Abhi/QA-HUB/qa-learning-hub')
    
    # Update pages in /pages/ directory (depth 1)
    pages_dir = base_dir / 'pages'
    for html_file in pages_dir.glob('*.html'):
        update_html_file(html_file, is_deep=False)
    
    # Update pages in /pages/learn/ directory (depth 2)
    learn_dir = pages_dir / 'learn'
    for html_file in learn_dir.glob('*.html'):
        update_html_file(html_file, is_deep=True)
    
    # Update pages in /pages/tools/ directory (depth 2)
    tools_dir = pages_dir / 'tools'
    for html_file in tools_dir.glob('*.html'):
        update_html_file(html_file, is_deep=True)
    
    print("\n✅ All pages updated successfully!")
    print("Premium design has been applied to all pages.")

if __name__ == '__main__':
    main()
