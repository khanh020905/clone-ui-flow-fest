import re

with open('/Users/macbookpro/clone-ui-about/index.html', 'r') as f:
    lines = f.readlines()

old_colors = ["#F97028", "#F489A3", "#F0BB0D", "#F3A20F"]
old_colors_lower = [c.lower() for c in old_colors]
new_colors = ["#D42518", "#F86015", "#FFCA26", "#9ABC04", "#19532B"]

current_block_last_line = -100
color_index = 0

for i, line in enumerate(lines):
    # Check if line contains a stroke color
    match = re.search(r'stroke="([^"]+)"', line)
    if match:
        color = match.group(1).upper()
        if color in old_colors:
            # If gap > 10, it's a new block
            if i - current_block_last_line > 10:
                color_index = 0
            
            # Replace
            new_color = new_colors[color_index % 5]
            lines[i] = line.replace(match.group(1), new_color)
            
            color_index += 1
            current_block_last_line = i

with open('/Users/macbookpro/clone-ui-about/index.html', 'w') as f:
    f.writelines(lines)

print("Rainbow colors updated.")
