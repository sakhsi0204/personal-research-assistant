from document_handler import (
    download_pdf,
    extract_text,
    save_text,
    get_pdf_stats
)

pdf_url = "https://arxiv.org/pdf/1706.03762.pdf"

pdf_path = download_pdf(
    pdf_url,
    "attention_is_all_you_need.pdf"
)

text = extract_text(pdf_path)

print("\nTEXT PREVIEW:\n")
print(text[:1000])

stats = get_pdf_stats(text)

print("\nPDF STATISTICS:")
print(stats)

save_text(
    text,
    "paper_text.txt"
)