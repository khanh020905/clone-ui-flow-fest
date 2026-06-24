import re

with open("index.html", "r") as f:
    html = f.read()

replacements = [
    ("Basic", "Hiểu đúng từ những điều cơ bản"),
    ("Pre-Foundation", "Nắm chắc những mảng trọng tâm"),
    ("Foundation", "Làm đúng từ những điều cốt lõi"),
    ("Advanced", "Chuyên sâu trong từng chi tiết"),
    ("Advanced 2 Skills", "Nâng tầm từng kỹ năng")
]

def repl(match):
    idx = getattr(repl, 'count', 0)
    if idx >= len(replacements):
        idx = 0
    
    title, subtext = replacements[idx]
    bg_div = match.group(1)
    
    new_html = f'''{bg_div}
                <div style="position: relative; z-index: 2; width: 100%; padding-left: 5%; display: flex; flex-direction: column; justify-content: center;">
                  <p class="expect-item_p" style="margin: 0; text-align: left;">{title}</p>
                  <p style="color: var(--color-light-plus); font-size: 1.125em; text-align: left; margin: 0.2rem 0 0 0; font-family: inherit;">{subtext}</p>
                </div>'''
    
    repl.count = idx + 1
    return new_html

# We want to replace `<div class="expect-item__bg..."></div> <p class="expect-item_p">...</p>`
# Notice that Live Music has `<br />` inside.
pattern = re.compile(r'(<div class="expect-item__bg[^>]+></div>)\s*<p class="expect-item_p">.*?</p>', re.DOTALL)

new_html = pattern.sub(repl, html)

with open("index.html", "w") as f:
    f.write(new_html)

print("Done")
