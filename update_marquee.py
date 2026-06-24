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
# We need to make sure we don't accidentally match beyond the item.
pattern = re.compile(r'(<div class="marquee-css__item">).*?(</div>\s*</div>\s*</div>)', re.DOTALL)
# Wait, the structure is:
# <div class="marquee-css__list">
#   <div class="marquee-css__item"> ... </div>
#   <div class="marquee-css__item"> ... </div>
# ...

pattern2 = re.compile(r'<div class="marquee-css__item">.*?<div class="marquee-css__dot"></div>\s*</div>', re.DOTALL)

# Let's verify the exact end of marquee-css__item.
# looking at the file, it ends with a dot or an SVG?
