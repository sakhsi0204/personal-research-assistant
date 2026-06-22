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
    try:
        doc = fitz.open(pdf_path)

        text = ""

        for page in doc:
            text += page.get_text()

        return text

    except Exception as e:
        print("Extraction Error:", e)
        return ""


def save_text(text, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)

    print("Text saved successfully")


def get_pdf_stats(text):
    return {
        "word_count": len(text.split()),
        "character_count": len(text)
    }


if __name__ == "__main__":
    print("PDF Downloader & Parser Module Ready")