with open('/Users/macbookpro/clone-ui-about/original.html', 'r') as f:
    orig = f.read()

start_marker = '<div class="welcome__row-cards">'
end_marker = '<div class="stacked-cards is--vertical">'

start_idx = orig.find(start_marker)
if start_idx != -1:
    end_idx = orig.find(end_marker, start_idx)
    correct_rainbow = orig[start_idx:end_idx]
    print(correct_rainbow)
