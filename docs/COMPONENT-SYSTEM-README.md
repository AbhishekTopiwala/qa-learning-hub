# QA Learning Hub - Component System

## Overview
The website now uses a **reusable component system** for the header and footer. This means you only need to update **one file** when making changes to the navigation or footer, instead of updating all 10 HTML files!

## How It Works

### Component Files
Located in `/includes/` folder:
- **`header.html`** - Contains the navigation header (with the Learn dropdown)
- **`footer.html`** - Contains the footer

### How to Update All Pages

#### To Update the Navigation/Header:
1. Edit **`includes/header.html`**
2. Save the file
3. The changes will automatically appear on ALL pages! ✨

#### To Update the Footer:
1. Edit **`includes/footer.html`**
2. Save the file  
3. The changes will automatically appear on ALL pages! ✨

## How to Use in HTML Files

### Step 1: Replace Header
**Replace this:**
```html
<header class="header">
    <nav class="container">
        <!-- ...all navigation code... -->
    </nav>
</header>
```

**With this:**
```html
<!-- Header Placeholder (loaded from includes/header.html) -->
<div id="header-placeholder"></div>
```

### Step 2: Replace Footer
**Replace this:**
```html
<footer class="footer">
    <div class="container">
        <!-- ...all footer code... -->
    </div>
</footer>
```

**With this:**
```html
<!-- Footer Placeholder (loaded from includes/footer.html) -->
<div id="footer-placeholder"></div>
```

### Step 3: Add Component Loader Script
Make sure your HTML file has BOTH scripts **before** the closing `</body>` tag:

```html
    <script src="js/components.js"></script>
    <script src="js/main.js"></script>
</body>
```

**Important:** `components.js` must come BEFORE `main.js`!

## Files to Update

You need to update these HTML files to use the component system:

- [x] `index.html` ✅ (Already done as example)
- [ ] `manual-testing.html`
- [ ] `api-testing.html`
- [ ] `automation.html`
- [ ] `roadmap.html`
- [ ] `practice.html`
- [ ] `interview.html`
- [ ] `resume.html`
- [ ] `about.html`
- [ ] `bug-library.html`

## Example: index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QA Learning Hub</title>
    <link rel="stylesheet" href="css/styles.css">
</head>

<body>

    <!-- Header Placeholder (loaded from includes/header.html) -->
    <div id="header-placeholder"></div>

    <!-- Your page content here -->
    <section class="hero">
        <!-- ... -->
    </section>

    <!-- Footer Placeholder (loaded from includes/footer.html) -->
    <div id="footer-placeholder"></div>

    <script src="js/components.js"></script>
    <script src="js/main.js"></script>
</body>
</html>
```

## Benefits

✅ **Update Once, Apply Everywhere** - Change header/footer in one place  
✅ **Cleaner HTML** - Less code duplication  
✅ **Easier Maintenance** - No need to update 10 files for minor changes  
✅ **Consistent Design** - All pages always have the same header/footer  

## Technical Details

- **`/js/components.js`** - Loads header.html and footer.html dynamically
- **`/js/main.js`** - Waits for components to load, then initializes all functionality
- Uses `fetch()` API to load HTML content
- Works with all modern browsers

## Notes

- The dropdown arrow is now on the **right side** of "Learn" ✨
- All dropdown functionality is preserved
- Mobile menu still works perfectly
- No changes to existing CSS or styling needed

---

**Need Help?** Just edit `includes/header.html` or `includes/footer.html` and save!
