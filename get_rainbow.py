with open('/Users/macbookpro/clone-ui-about/original.html', 'r') as f:
    content = f.read()

# find rainbow-vertical__1
idx = content.find('<div class="rainbow-vertical__1">')
if idx != -1:
    end_idx = content.find('</div>\n                  <div class="stacked-cards is--vertical">', idx)
    rainbow_html = content[idx:end_idx+6]
    print(rainbow_html)
else:
    print("Not found")
