from PyPDF2 import PdfReader
from io import BytesIO

def extract_text_from_pdfs(pdf_files):
    text = ""
    for pdf in pdf_files:
        pdf_reader = PdfReader(BytesIO(pdf))
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text
