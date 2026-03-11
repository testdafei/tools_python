import pdfplumber

pdf_path = "离线资源方案.pdf"
output_path = "离线资源方案_文本提取.txt"

with pdfplumber.open(pdf_path) as pdf:
    all_text = ""
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        if text:
            all_text += f"\n\n--- 第{i+1}页 ---\n\n"
            all_text += text

with open(output_path, "w", encoding="utf-8") as f:
    f.write(all_text)

print(f"提取完成，文本已保存至 {output_path}")