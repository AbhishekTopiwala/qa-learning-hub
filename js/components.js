// ================================================
// Component Loader - Load Header and Footer (UPDATED v2)
// ================================================

// Function to get the base path based on current page location
function getBasePath() {
    const path = window.location.pathname;
    
    // Count how many levels deep we are
    const pathParts = path.split('/').filter(p => p && p.endsWith('.html'));
    
    // If path includes pages/learn/ or pages/tools/ (2 levels deep in pages)
    if (path.includes('/pages/learn/') || path.includes('/pages/tools/')) {
        return '../../';
    }
    // If path includes just /pages/ (1 level deep in pages)
    else if (path.includes('/pages/')) {
        return '../';
    }
    // If at root or just filename
    else {
        return './';
    }
}

// Function to load HTML components with dynamic base path
async function loadComponent(elementId, filePath) {
    try {
        const basePath = getBasePath();
        const fullPath = basePath + filePath;
        
        console.log(`Loading component from: ${fullPath}`);
        
        const response = await fetch(fullPath);
        if (!response.ok) {
            throw new Error(`Failed to load ${fullPath}`);
        }
        const html = await response.text();
        const element = document.getElementById(elementId);
        if (element) {
            element.innerHTML = html;
            
            // After loading, fix all navigation links based on current location
            fixNavigationLinks(basePath);
        }
    } catch (error) {
        console.error('Error loading component:', error);
    }
}

// Fix navigation links to work from current page location  
function fixNavigationLinks(basePath) {
    console.log(`Fixing navigation links with base path: ${basePath}`);
    
    // Fix all links in header and footer
    document.querySelectorAll('#header-placeholder a, #footer-placeholder a').forEach(link => {
        const href = link.getAttribute('href');
        
        // Skip if it's a hash link or already has base path or is http/https
        if (!href || href.startsWith('#') || href.startsWith('http') || href.startsWith(basePath)) {
            return;
        }
        
        // Apply the correct base path
        const newHref = basePath + href;
        link.setAttribute('href', newHref);
        console.log(`Updated link: ${href} → ${newHref}`);
    });
    
    console.log('✅ Navigation links fixed!');
}

// Load header and footer when DOM is ready
document.addEventListener('DOMContentLoaded', async function() {
    console.log('🔄 Loading components...');
    console.log('Current location:', window.location.pathname);
    
    // Load header and footer
    await loadComponent('header-placeholder', 'includes/header.html');
    await loadComponent('footer-placeholder', 'includes/footer.html');
    
    console.log('✅ Components loaded successfully!');
    
    // After loading, initialize the main.js functionality
    window.dispatchEvent(new Event('componentsLoaded'));
});
