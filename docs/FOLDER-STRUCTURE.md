# 📂 Organized Folder Structure

## Overview
The QA Learning Hub project now has a clean, professional folder structure that separates content by purpose and makes the codebase easy to navigate.

---

## 📁 Directory Structure

```
qa-website/
├── index.html                          # Homepage (root level)
│
├── assets/                             # Static assets
│   └── icons/                          # Icon files
│
├── backups/                            # Backup files
│   ├── about.html.backup
│   ├── api-testing.html.backup
│   ├── automation.html.backup
│   ├── bug-library.html.backup
│   ├── interview.html.backup
│   ├── manual-testing.html.backup
│   ├── practice.html.backup
│   ├── resume.html.backup
│   └── roadmap.html.backup
│
├── css/                                # Stylesheets
│   └── styles.css                      # Main stylesheet
│
├── docs/                               # Documentation
│   ├── COMPONENT-SYSTEM-README.md      # Component system guide
│   ├── QUICK-REFERENCE.md              # Quick reference card
│   ├── REUSABLE-CODE-GUIDE.md          # Reusable code guide
│   └── REUSABLE-CODE-SUMMARY.md        # Implementation summary
│
├── includes/                           # Reusable components
│   ├── header.html                     # Navigation header
│   └── footer.html                     # Page footer
│
├── js/                                 #  JavaScript files
│   ├── components.js                   # Component loader
│   └── main.js                         # Main application logic
│
├── pages/                              # All web pages (organized)
│   ├── learn/                          # Learning content pages
│   │   ├── manual-testing.html         # Manual testing guide
│   │   ├── automation.html             # Automation testing guide
│   │   └── api-testing.html            # API testing guide
│   │
│   ├── tools/                          # QA tools and resources
│   │   ├── practice.html               # Practice zone
│   │   ├── interview.html              # Interview preparation
│   │   ├── resume.html                 # Resume & career guide
│   │   └── bug-library.html            # Bug report examples
│   │
│   ├── about.html                      # About page
│   └── roadmap.html                    # QA roadmap
│
├── scripts/                            # Utility scripts
│   ├── update_components.py            # Component migration script
│   ├── update_paths.py                 # Path updater script
│   └── update-to-components.sh         # Shell migration script
│
├── templates/                          # HTML templates
│   └── base-template.html              # Base page template
│
└── favicon.png                         # Site favicon
```

---

## 🗂️ Folder Purposes

### `/` (Root)
- **index.html** - Main homepage, stays at root for easy access

### `/assets/`
- Static assets like icons, images, fonts
- Organized by type (icons, images, etc.)

### `/backups/`
- All `.backup` files from component migration
- Safe to delete after verifying everything works
- Keep for rollback if needed

### `/css/`
- All stylesheet files
- Currently contains `styles.css` (main stylesheet)

### `/docs/`
- All project documentation
- README files, guides, references
- Easy to find and maintain

### `/includes/`
- **Reusable HTML components**
- `header.html` - Used on every page
- `footer.html` - Used on every page

### `/js/`
- JavaScript files
- `components.js` - Dynamically loads header/footer
- `main.js` - Main application logic

### `/pages/`
Main content pages, organized by category:

#### `/pages/learn/`
Educational content about testing:
- Manual Testing Guide
- Automation Testing Guide
- API Testing Guide

#### `/pages/tools/`
QA resources and tools:
- Practice Zone
- Interview Preparation
- Resume & Career Guide
- Bug Report Library

#### `/pages/` (root)
General pages:
- About
- Roadmap

### `/scripts/`
- Python and shell scripts
- Migration and utilities
- Not served to users

### `/templates/`
- HTML templates for creating new pages
- Base templates with placeholders

---

## 🔗 URL Structure

### Homepage
```
https://yoursite.com/index.html
```

### Learn Pages
```
https://yoursite.com/pages/learn/manual-testing.html
https://yoursite.com/pages/learn/automation.html
https://yoursite.com/pages/learn/api-testing.html
```

### Tools Pages
```
https://yoursite.com/pages/tools/practice.html
https://yoursite.com/pages/tools/interview.html
https://yoursite.com/pages/tools/resume.html
https://yoursite.com/pages/tools/bug-library.html
```

### General Pages
```
https://yoursite.com/pages/about.html
https://yoursite.com/pages/roadmap.html
```

---

## ✅ Benefits of This Structure

### 1. **Logical Organization**
- Content grouped by purpose
- Easy to find specific pages
- Clear hierarchy

### 2. **Scalability**
- Easy to add new pages to appropriate folders
- Can add new categories (e.g., `/pages/advanced/`)
- Room for growth

### 3. **Maintainability**
- Documentation in one place (`/docs/`)
- Scripts in one place (`/scripts/`)
- Components in one place (`/includes/`)

### 4. **Professional Structure**
- Follows industry best practices
- Clean and organized
- Easy for new developers to understand

### 5. **SEO Benefits**
- Descriptive URLs (e.g., `/pages/learn/api-testing.html`)
- Logical content hierarchy
- Better for search engines

---

## 📝 Path Updates

All files have been automatically updated with correct paths:

### Component Paths
- Learn pages: `../../includes/header.html`
- Tools pages: `../../includes/header.html`
- General pages: `../includes/header.html`

### Asset Paths
- Learn pages: `../../css/styles.css`, `../../js/main.js`
- Tools pages: `../../css/styles.css`, `../../js/main.js`
- General pages: `../css/styles.css`, `../js/main.js`

### Navigation Links
All navigation links updated to use relative paths based on current location.

---

## 🚀 Next Steps

### Testing
1. Open `index.html` in browser
2. Navigate to each page
3. Verify all links work
4. Check that all styles and scripts load

### Cleanup (Optional)
Once everything is verified:
```bash
cd qa-website
rm -rf backups/  # Remove backup files
```

### Adding New Pages

#### New Learn Page
```bash
cp templates/base-template.html pages/learn/new-topic.html
# Edit the file
# Paths will be: ../../css/, ../../js/, etc.
```

#### New Tool Page
```bash
cp templates/base-template.html pages/tools/new-tool.html  
# Edit the file
# Paths will be: ../../css/, ../../js/, etc.
```

---

## 📊 Statistics

### Before Organization
- All files in root directory
- 10 HTML pages + 9 backups + docs + scripts = Messy!
- Hard to navigate
- No logical grouping

### After Organization
- ✅ 6 organized folders
- ✅ Clean root (just index.html + favicon)
- ✅ Logical categorization
- ✅ Professional structure
- ✅ Easy to navigate
- ✅ Room to scale

### Files Moved
- 📄 9 HTML pages → `/pages/` subdirectories
- 📦 9 backup files → `/backups/`
- 📚 4 documentation files → `/docs/`
- 🔧 3 script files → `/scripts/`

---

## 🎯 Quick Reference

### Find Documentation
```
📂 docs/
```

### Find Learn Content
```
📂 pages/learn/
```

### Find Tools & Resources
```
📂 pages/tools/
```

### Find Components
```
📂 includes/
```

### Find Scripts
```
📂 scripts/
```

---

**Last Updated:** January 19, 2026  
**Structure Version:** 2.0  
**Status:** ✅ Production Ready
