import re

with open("index.html", "r") as f:
    html = f.read()

# Images to use
images = [
    "student/6.png",
    "student/7.png",
    "student/8.png",
    "student/9.png",
    "student/10.png",
    "student/Your paragraph text (6).png"
]

def repl(match):
    idx = getattr(repl, 'count', 0)
    if idx >= len(images):
        idx = 0
    
    img_path = images[idx]
    
    # We replace the img and optionally the community-tag
    new_card = f'''<div class="community-card__before"></div>
                    <img
                      src="{img_path}"
                      loading="lazy" width="256.5" alt="" class="cover-image" />'''
    
    repl.count = idx + 1
    return new_card

# Regex to match the inside of community-card
pattern = re.compile(r'<div class="community-card__before"></div>\s*<img\s+src="[^"]+"[^>]+>\s*(<div class="community-tag">\s*<span[^>]*>[^<]+</span>\s*</div>)?', re.DOTALL)

new_html = pattern.sub(repl, html)

with open("index.html", "w") as f:
    f.write(new_html)

print("Done")
