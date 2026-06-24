# Website UI Cloning Skill

This document provides a comprehensive guide and standard operating procedure for cloning a website's User Interface (UI).

## 1. Prerequisites & Assets Required

Before starting the coding process, gather the following essential components from the target website:

*   **HTML Structure:** The DOM structure, classes, IDs, and semantic tags.
*   **CSS Styling:** All inline styles, internal `<style>` tags, and external stylesheets (including global resets, framework CSS, and custom styles).
*   **Media Assets:** Images (JPG, PNG, SVG), background videos, icons, and logos.
*   **Typography:** Custom fonts (e.g., Google Fonts, `.woff`, `.woff2` files).
*   **JavaScript (Optional but recommended for full UX):** Libraries for animations (e.g., GSAP), layout transitions, and interactive components.

## 2. Step-by-Step Execution Plan

### Step 1: Base HTML Setup
1. Create a clean `index.html` file.
2. Extract the exact `<head>` content from the target website. This is **critical** because the `<head>` contains:
    *   Meta tags for responsive design (`viewport`).
    *   Links to external CSS bundles (which contain global layout rules and webfonts).
    *   Links to external font families (like Google Fonts).
    *   Links to external JS libraries required for rendering.

### Step 2: Injecting the Content (DOM)
1. Copy the `<body>` content from the target site (or the specific components you want to clone, such as headers, hero sections, footers).
2. Ensure all `class` and `id` attributes remain exactly as they were in the original, as the CSS heavily relies on them.

### Step 3: Applying Custom Styles
1. If there are any custom CSS variables or overrides (e.g., a `style.md` file provided), wrap them correctly.
    *   Global CSS variables (e.g., `--color-primary`, `--container-padding`) should be wrapped in `:root { ... }` or `body { ... }`.
    *   Component-specific styles should target the exact classes extracted in Step 2.
2. Merge these custom styles into a `<style>` block directly above the closing `</head>` tag, ensuring they take precedence over the base external stylesheets.

### Step 4: Asset Linking and Validation
1. Verify that all `<img>` tags, `<svg>` elements, and background images have valid URLs. If they were relative paths in the original site, convert them to absolute URLs pointing to the original domain, or download them locally and update the paths.
2. Verify that font families specified in the CSS are successfully loading via the network tab.

### Step 5: Interactivity (JavaScript)
1. If the UI requires animations or dynamic behaviors, include the necessary script tags (e.g., `<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>`) at the end of the `<body>`.
2. Replicate the initialization scripts. (Note: If the original site uses an obfuscated framework like React/Vue, you may need to manually recreate the interactions using Vanilla JS or GSAP).

## 3. Best Practices & Troubleshooting

*   **100% Exact Match:** If the clone doesn't match the original exactly, the most common culprit is missing global CSS resets or missing external typography. Always check the original `<head>` for missing `<link rel="stylesheet">`.
*   **Broken Layouts:** Check for missing wrapper `<div>` elements. A single missing closing tag or parent container can break Flexbox or Grid layouts.
*   **Invalid CSS Variables:** Watch out for syntax errors in CSS variables (e.g., accidentally deleted characters or invalid variable names).
*   **CORS Issues:** Some external fonts or assets might block cross-origin requests. In such cases, download the assets locally.

## 4. Automation Script (Python)
If you have the original HTML and custom styles separated, use a script to merge them programmatically:

```python
def merge_clone():
    with open('style.css', 'r') as f: styles = f.read()
    with open('head.html', 'r') as f: head = f.read()
    with open('body.html', 'r') as f: body = f.read()
    
    # Inject styles before closing head
    head = head.replace('</head>', f'<style>:root {{ {styles} }}</style></head>')
    
    full_html = f"<!DOCTYPE html>\n<html lang='en'>\n{head}\n{body}\n</html>"
    with open('index.html', 'w') as f: f.write(full_html)
```
