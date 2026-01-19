# QA Learning Hub Website

Learn Quality Assurance the practical way - from beginner to job-ready QA professional.

## 🚀 Quick Start

1. **Open the website:**
   ```bash
   # Open in browser
   open index.html
   # or
   firefox index.html
   ```

2. **Local Development:**
   - No build process required
   - Pure HTML, CSS, and JavaScript
   - Just open `index.html` in your browser

## 📂 Project Structure

```
qa-website/
├── index.html              # Homepage
├── favicon.png             # Site icon
│
├── pages/                  # All content pages
│   ├── learn/             # Learning guides
│   ├── tools/             # QA tools & resources
│   ├── about.html         # About page
│   └── roadmap.html       # QA roadmap
│
├── includes/              # Reusable components
│   ├── header.html        # Navigation
│   └── footer.html        # Footer
│
├── css/                   # Stylesheets
├── js/                    # JavaScript
├── docs/                  # Documentation
├── scripts/               # Utility scripts
└── templates/             # Page templates
```

For detailed structure: see [docs/FOLDER-STRUCTURE.md](docs/FOLDER-STRUCTURE.md)

## 📚 Documentation

- **[Folder Structure](docs/FOLDER-STRUCTURE.md)** - Complete directory organization
- **[Component System](docs/COMPONENT-SYSTEM-README.md)** - How to use components
- **[Reusable Code Guide](docs/REUSABLE-CODE-GUIDE.md)** - Architecture details
- **[Quick Reference](docs/QUICK-REFERENCE.md)** - Common tasks

## ✏️ Making Changes

### Update Navigation (All Pages)
```bash
# Edit ONE file - changes apply to ALL pages
nano includes/header.html
```

### Update Footer (All Pages)
```bash
nano includes/footer.html
```

### Add New Page
```bash
# Copy template
cp templates/base-template.html pages/learn/new-topic.html

# Edit as needed
nano pages/learn/new-topic.html
```

## 🌐 Page URLs

### Homepage
- `/index.html`

### Learn Pages
- `/pages/learn/manual-testing.html`
- `/pages/learn/automation.html`
- `/pages/learn/api-testing.html`

### Tools & Resources
- `/pages/tools/practice.html`
- `/pages/tools/interview.html`
- `/pages/tools/resume.html`
- `/pages/tools/bug-library.html`

### General
- `/pages/about.html`
- `/pages/roadmap.html`

## 🎨 Features

- ✅ **Component-Based** - Reusable header/footer
- ✅ **Modern Design** - Gradient theme, smooth animations
- ✅ **Responsive** - Works on mobile, tablet, desktop
- ✅ **Organized** - Clean folder structure
- ✅ **Documented** - Comprehensive guides
- ✅ **No Build** - Pure HTML/CSS/JS
- ✅ **Fast** - Lightweight and optimized

## 🛠️ Technology Stack

- **HTML5** - Semantic markup
- **CSS3** - Modern styling with gradients, animations
- **Vanilla JavaScript** - No frameworks needed
- **Component System** - Dynamic header/footer loading

## 📊 Statistics

- **10 Pages** - Comprehensive QA content
- **2 Components** - Header & Footer
- **1 Stylesheet** - ~1300 lines of organized CSS
- **2 JS Files** - Components + Main logic
- **~800 Lines** - Removed through componentization
- **90% Faster** - Updates via component system

## 🔧 Maintenance

### Common Tasks

#### Update All Navigation Links
```bash
vim includes/header.html  # Edit navigation
# Changes apply automatically to all 10 pages!
```

#### Add New Page Type
```bash
mkdir pages/new-category
cp templates/base-template.html pages/new-category/page.html
```

#### Clean Backup Files
```bash
rm -rf backups/  # After verifying everything works
```

## 🎯 Development Workflow

1. **Make changes** to components or pages
2. **Test** in browser (refresh to see changes)
3. **Commit** changes if using Git
4. **Deploy** - upload entire folder to web server

## 📱 Browser Support

- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Mobile browsers

## 🚀 Deployment

### Deploy to Web Host
```bash
# Upload entire qa-website folder via FTP/SFTP
# Or use hosting panel file manager
```

### Deploy to GitHub Pages
```bash
git add .
git commit -m "Update website"
git push origin main
```

### Deploy to Netlify/Vercel
- Simply drag and drop the `qa-website` folder
- Or connect your Git repository

## 📈 Performance

- **Page Size**: ~20-50KB per page
- **Load Time**: < 1 second
- **HTTP Requests**: ~5-7 per page
- **Optimized**: Minimal CSS/JS, efficient images

## 🤝 Contributing

1. Create a new page using the template
2. Follow the existing naming conventions
3. Update navigation in `includes/header.html`
4. Test across all pages
5. Document your changes

## 📝 License

© 2026 QA Learning Hub. Built by QA professionals, for QA learners.

## 💡 Tips

- **Consistent Naming**: Use lowercase with hyphens (e.g., `api-testing.html`)
- **Component System**: Always load via placeholders, never duplicate
- **Test Changes**: Check on multiple pages before deploying
- **Keep Backups**: The `/backups/` folder has all originals

## 🆘 Troubleshooting

### Pages not loading?
- Check file paths are correct
- Verify `components.js` is loading
- Open browser console (F12) for errors

### Styles missing?
- Clear browser cache (Ctrl+F5)
- Check CSS file path
- Verify `styles.css` exists

### Navigation broken?
- Check `includes/header.html` paths
- Verify component loader is working
- Test from different page locations

## 📞 Support

For detailed documentation, see:
- [docs/FOLDER-STRUCTURE.md](docs/FOLDER-STRUCTURE.md)
- [docs/REUSABLE-CODE-GUIDE.md](docs/REUSABLE-CODE-GUIDE.md)

---

**Current Version**: 2.0  
**Last Updated**: January 19, 2026  
**Status**: ✅ Production Ready
