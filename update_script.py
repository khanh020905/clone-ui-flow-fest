import re

with open('slater_script.js', 'r') as f:
    js = f.read()

js = js.replace('"Hi Friends!"', '"Welcome to TID!"')
js = js.replace('"We are back..."', '"cùng khám phá nhé..."')

with open('main.js', 'w') as f:
    f.write(js)

print("JS updated")
