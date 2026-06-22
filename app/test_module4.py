from document_handler import *

pdf_url = "https://arxiv.org/pdf/1706.03762.pdf"

pdf_path = download_pdf(
    pdf_url,
    "attention_is_all_you_need.pdf"
)

page_texts = extract_text(pdf_path)

print("\nFIRST PAGE PREVIEW:\n")

print(page_texts[1][:1000])

stats = get_pdf_stats(page_texts)

print("\nPDF STATISTICS:\n")

print(stats)

save_text(
    page_texts,
    "paper_text.txt"
)