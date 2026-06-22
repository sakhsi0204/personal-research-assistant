import fitz
import urllib.request
import os

PDF_FOLDER = "pdf_cache"

def download_pdf(pdf_url, filename):
    """
    Download PDF from URL and save locally
    """
    if not os.path.exists(PDF_FOLDER):
        os.makedirs(PDF_FOLDER)

    filepath = os.path.join(PDF_FOLDER, filename)

    urllib.request.urlretrieve(pdf_url, filepath)

    return filepath


def extract_text(pdf_path):
    """
    Extract text from PDF
    """
    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    return text


if __name__ == "__main__":
    print("PDF Downloader & Parser Module Ready")