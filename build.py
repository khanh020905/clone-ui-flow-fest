import os

def build_html():
    style_path = '/Users/macbookpro/clone-ui-about/style.md'
    html_path = '/Users/macbookpro/clone-ui-about/outer-html.md'
    head_path = '/Users/macbookpro/clone-ui-about/extracted_head.html'
    output_path = '/Users/macbookpro/clone-ui-about/index.html'

    with open(style_path, 'r', encoding='utf-8') as f:
        style_content = f.read()

    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    with open(head_path, 'r', encoding='utf-8') as f:
        head_content = f.read()

    head_content = head_content.replace('</head>', f"""
    <style>
:root, body {{
{style_content}
}}
    </style>
</head>""")

    full_html = f"""<!DOCTYPE html>
<html lang="en">
{head_content}
{html_content}
</html>
"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print("Built index.html successfully.")

if __name__ == "__main__":
    build_html()
