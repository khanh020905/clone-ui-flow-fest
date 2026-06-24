import re

with open('index.html', 'r') as f:
    content = f.read()

# Remove the nav element
new_content = re.sub(r'\s*<nav class="nav">.*?</nav>', '', content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(new_content)

print("Nav removed")
