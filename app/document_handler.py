import fitz
import urllib.request
import os

PDF_FOLDER = "pdf_cache"


def download_pdf(pdf_url, filename):
    try:
        if not os.path.exists(PDF_FOLDER):
            os.makedirs(PDF_FOLDER)

        filepath = os.path.join(PDF_FOLDER, filename)

        urllib.request.urlretrieve(pdf_url, filepath)

        print(f"Downloaded: {filename}")

        return filepath

    except Exception as e:
        print("Download Error:", e)

def extract_text(pdf_path):

    doc = fitz.open(pdf_path)

    page_texts = {}

    for page_num in range(len(doc)):

        page = doc.load_page(page_num)

        text = page.get_text()

        page_texts[page_num + 1] = text

    doc.close()

    return page_texts


def save_text(page_texts, filename):

    with open(filename, "w", encoding="utf-8") as file:

        for page_num, text in page_texts.items():

            file.write(f"\n===== PAGE {page_num} =====\n")

            file.write(text)

    print("Text saved successfully")


def get_pdf_stats(page_texts):

    total_pages = len(page_texts)

    total_words = 0

    for text in page_texts.values():

        total_words += len(text.split())

    return {
        "pages": total_pages,
        "words": total_words
    }


if __name__ == "__main__":
    print("PDF Downloader & Parser Module Ready")