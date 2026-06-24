import urllib.request
import re

url = "http://theieltsdictionary.com/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')

# Search for background-image, grid, linear-gradient
matches = re.findall(r'style="[^"]*"', html)
for m in set(matches):
    if 'background' in m or 'grid' in m or 'gradient' in m:
        print("Inline:", m)

# Find CSS chunks
for link in re.findall(r'href="(/_next/static/css/[^"]+\.css)"', html) + re.findall(r'href="(/_next/static/chunks/[^"]+\.css)"', html):
    css_url = "http://theieltsdictionary.com" + link
    css = urllib.request.urlopen(css_url).read().decode('utf-8')
    # Print lines containing bg- or grid or linear-gradient
    for match in re.findall(r'\.[a-zA-Z0-9_-]+(?:\{[^}]*background[^}]*\}|\{[^}]*gradient[^}]*\}|\{[^}]*grid[^}]*\})', css):
        if 'bg-radiate' in match or 'herb' in match or 'gradient' in match or 'grid' in match:
            print("CSS rule:", match)

