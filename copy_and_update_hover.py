import re
import os
import shutil

source_dir = "drive-download-20260624T082056Z-3-001"
dest_dir = "images"

# 5 images to use
selected_images = [
    "BEN WISEMAN.jpeg",
    "Dan Bejar.jpeg",
    "Creative Social Illustrations.jpeg",
    "Great stories stretch minds.jpeg",
    "When in doubt, pick up a book_.jpeg"
]

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

new_image_paths = []
for i, img_name in enumerate(selected_images):
    src = os.path.join(source_dir, img_name)
    dst_name = f"hover{i+1}.jpeg"
    dst = os.path.join(dest_dir, dst_name)
    shutil.copy(src, dst)
    new_image_paths.append(dst)

with open("index.html", "r") as f:
    html = f.read()

def repl(match):
    idx = getattr(repl, 'count', 0)
    if idx >= len(new_image_paths):
        idx = 0
    
    img_path = new_image_paths[idx]
    
    new_html = f'<img src="{img_path}" loading="lazy" width="540" alt="" class="cover-image" />'
    
    repl.count = idx + 1
    return new_html

# The images are inside <div class="expect-card">...</div>
# Let's match `<img src="[^"]+" loading="lazy" width="540" alt="" class="cover-image" />`
pattern = re.compile(r'<img\s+src="[^"]+"\s+loading="lazy"\s+width="540"\s+alt=""\s+class="cover-image"\s*/>')

new_html = pattern.sub(repl, html)

with open("index.html", "w") as f:
    f.write(new_html)

print("Done")
