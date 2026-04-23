import pdfplumber
from docx import Document
from PIL import Image
import pytesseract
import io

def read_file(filename, content):
    if filename.endswith(".pdf"):
        with pdfplumber.open(io.BytesIO(content)) as pdf:
            return "\n".join([p.extract_text() or "" for p in pdf.pages])

    elif filename.endswith(".docx"):
        doc = Document(io.BytesIO(content))
        return "\n".join([p.text for p in doc.paragraphs])

    elif filename.endswith(".png") or filename.endswith(".jpg"):
        img = Image.open(io.BytesIO(content))
        return pytesseract.image_to_string(img)

    else:
        return content.decode("utf-8")