import re

with open("/Users/macbookpro/clone-ui-about/index.html", "r") as f:
    html = f.read()

qa_pairs = [
    ("Tôi chưa từng học IELTS, có học được không?", "Có. TID có các khoá học từ Basic đến Advanced và sẽ kiểm tra đầu vào miễn phí để xây dựng lộ trình phù hợp với trình độ hiện tại của bạn."),
    ("Lịch học tại TID như thế nào?", "Các lớp học tại TID diễn ra 2 buổi mỗi tuần, với hai khung giờ phổ biến là 18:30 và 20:30, giúp học sinh, sinh viên và người đi làm dễ dàng sắp xếp thời gian học."),
    ("Một lớp có bao nhiêu học viên?", "TID cam kết sĩ số không vượt quá 13 học viên để đảm bảo mỗi bạn đều nhận được sự hỗ trợ cần thiết từ giáo viên."),
    ("Ai sẽ trực tiếp giảng dạy?", "Các lớp học được dẫn dắt bởi đội ngũ giáo viên giàu kinh nghiệm với thành tích từ 8.5–9.0 IELTS và được đào tạo chuyên môn bài bản."),
    ("Nếu tôi nghỉ học một buổi thì sao?", "Trung tâm sẽ hỗ trợ học bù hoặc cung cấp tài liệu và hướng dẫn cần thiết để bạn không bị bỏ lỡ kiến thức."),
    ("TID hỗ trợ học viên ngoài giờ học như thế nào?", "Bên cạnh giờ học trên lớp, học viên được hỗ trợ giải đáp thắc mắc, chữa bài và sử dụng nền tảng học tập độc quyền của TID để tự học hiệu quả hơn.")
]

# Extract all list items
pattern = r'(<li\s+data-accordion-status="not-active"\s+class="accordion-css__item">.*?</svg>\s*</div>\s*</div>\s*</li>)'
matches = list(re.finditer(pattern, html, flags=re.DOTALL))

# Use the SECOND item as template because it doesn't have the button
template_item = matches[1].group(1)

new_items_html = ""
for q, a in qa_pairs:
    item_html = template_item
    
    # Replace the paragraph text
    item_html = re.sub(r'(<p class="accordion-css__item-p">)(.*?)(</p>)', r'\1' + a + r'\3', item_html, flags=re.DOTALL)
    
    # Replace the question text
    item_html = re.sub(r'(<h3 class="accordion-css__item-h3">\s*<strong>)(.*?)(</strong>\s*</h3>)', r'\1' + q + r'\3', item_html, flags=re.DOTALL)
    
    new_items_html += item_html + "\n"

# Replace the entire block
start_idx = matches[0].start()
end_idx = matches[-1].end()

new_html = html[:start_idx] + new_items_html + html[end_idx:]

with open("/Users/macbookpro/clone-ui-about/index.html", "w") as f:
    f.write(new_html)

print("FAQ fixed successfully.")
