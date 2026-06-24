import re

with open('index.html', 'r') as f:
    content = f.read()

new_item_content = """
              <p class="marquee-css__item-p">The IELTS Dictionary</p>
              <div class="marquee-css__dot"></div>
              <p class="marquee-css__item-p">The IELTS Dictionary</p>
              <div class="marquee-css__dot"></div>
              <p class="marquee-css__item-p">The IELTS Dictionary</p>
              <div class="marquee-css__dot"></div>"""

# Find all <div class="marquee-css__item">...</div> and replace contents
# the .*? will match everything until the next </div> that corresponds to it,
# but we need to be careful with nested divs.
# The structure is simple: no nested divs inside the item except the dots, which are <div class="marquee-css__dot"></div>
# So we can match up to `<div class="marquee-css__dot"></div>\n            </div>`

pattern = re.compile(r'<div class="marquee-css__item">.*?<div class="marquee-css__dot"></div>\s*</div>', re.DOTALL)

# Let's count how many we find
matches = pattern.findall(content)
print(f"Found {len(matches)} marquee items to replace")

# Perform replacement
new_html = pattern.sub(f'<div class="marquee-css__item">{new_item_content}\n            </div>', content)

with open('index.html', 'w') as f:
    f.write(new_html)

print("Marquee updated")
