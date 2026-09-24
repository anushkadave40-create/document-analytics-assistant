from PyPDF2 import PdfReader

def extract_text(pdf_files):
    text = ""

    for pdf in pdf_files:
        reader = PdfReader(pdf)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text