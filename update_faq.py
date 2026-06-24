import re

with open("/Users/macbookpro/clone-ui-about/index.html", "r") as f:
    html = f.read()

# The 6 new Q&A pairs
qa_pairs = [
    ("Tôi chưa từng học IELTS, có học được không?", "Có. TID có các khoá học từ Basic đến Advanced và sẽ kiểm tra đầu vào miễn phí để xây dựng lộ trình phù hợp với trình độ hiện tại của bạn."),
    ("Lịch học tại TID như thế nào?", "Các lớp học tại TID diễn ra 2 buổi mỗi tuần, với hai khung giờ phổ biến là 18:30 và 20:30, giúp học sinh, sinh viên và người đi làm dễ dàng sắp xếp thời gian học."),
    ("Một lớp có bao nhiêu học viên?", "TID cam kết sĩ số không vượt quá 13 học viên để đảm bảo mỗi bạn đều nhận được sự hỗ trợ cần thiết từ giáo viên."),
    ("Ai sẽ trực tiếp giảng dạy?", "Các lớp học được dẫn dắt bởi đội ngũ giáo viên giàu kinh nghiệm với thành tích từ 8.5–9.0 IELTS và được đào tạo chuyên môn bài bản."),
    ("Nếu tôi nghỉ học một buổi thì sao?", "Trung tâm sẽ hỗ trợ học bù hoặc cung cấp tài liệu và hướng dẫn cần thiết để bạn không bị bỏ lỡ kiến thức."),
    ("TID hỗ trợ học viên ngoài giờ học như thế nào?", "Bên cạnh giờ học trên lớp, học viên được hỗ trợ giải đáp thắc mắc, chữa bài và sử dụng nền tảng học tập độc quyền của TID để tự học hiệu quả hơn.")
]

# We want to replace the list items.
# Let's extract the template of an li item.
pattern = r'(<li\s+data-accordion-status="not-active"\s+class="accordion-css__item">.*?</svg>\s*</div>\s*</div>\s*</li>)'
matches = list(re.finditer(pattern, html, flags=re.DOTALL))

if not matches:
    print("Could not find list items.")
    exit(1)

template_item = matches[0].group(1)

new_items_html = ""
for i, (q, a) in enumerate(qa_pairs):
    # For the first one, there was a button inside, let's just replace the p tags and remove the button wrap.
    # We will use regex to replace the content of accordion-css__card
    item_html = template_item
    
    # Replace the card content
    card_pattern = r'(<div class="accordion-css__card">)(.*?)(</div>\s*</div>\s*</div>\s*</div>)'
    new_card_content = f'\n                          <p class="accordion-css__item-p">{a}</p>\n                        '
    item_html = re.sub(card_pattern, r'\1' + new_card_content + r'\3', item_html, flags=re.DOTALL)
    
    # Replace the question text
    q_pattern = r'(<h3 class="accordion-css__item-h3">\s*<strong>).*?(</strong>\s*</h3>)'
    item_html = re.sub(q_pattern, r'\1' + q + r'\2', item_html, flags=re.DOTALL)
    
    new_items_html += item_html + "\n"

# Now replace the whole block of existing lis with new_items_html
start_idx = matches[0].start()
end_idx = matches[-1].end()

new_html = html[:start_idx] + new_items_html + html[end_idx:]

with open("/Users/macbookpro/clone-ui-about/index.html", "w") as f:
    f.write(new_html)

print("FAQ updated successfully.")
