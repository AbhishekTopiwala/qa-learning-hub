# 🚀 Quick Reference - Reusable Components

## Common Tasks

### ✏️ Update Navigation Menu
```bash
File: includes/header.html
What: Edit once, applies to all 10 pages
```

### ✏️ Update Footer
```bash
File: includes/footer.html  
What: Edit once, applies to all 10 pages
```

### ➕ Add New Page
```bash
cp templates/base-template.html my-new-page.html
# Edit placeholders in my-new-page.html
```

### 🔧 Add Navigation Link
```html
<!-- includes/header.html -->
<li class="nav-item">
  <a href="new-page.html" class="nav-link">New Page</a>
</li>
```

### 📱 Icons Used
- 📝 Manual Testing
- 🤖 Automation Testing
- 🌐 API Testing

## Files That Load Components
All 10 HTML pages automatically load:
- `includes/header.html` (navigation)
- `includes/footer.html` (footer)

## Scripts Order
```html
<script src="js/components.js"></script>  <!-- Load components -->
<script src="js/main.js"></script>        <!-- Initialize app -->
```

## Need Help?
- Full docs: `REUSABLE-CODE-GUIDE.md`
- Quick start: `COMPONENT-SYSTEM-README.md`
- Summary: `REUSABLE-CODE-SUMMARY.md`
