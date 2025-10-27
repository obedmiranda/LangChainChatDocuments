import fitz  # PyMuPDF
def read_pdf_content(content: bytes) -> str:
  
    text = ""
    pdf = fitz.open(stream=content, filetype="pdf")
    for page in pdf:
        text += page.get_text()
    pdf.close()
    return text