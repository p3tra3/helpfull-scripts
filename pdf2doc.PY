import os
import pdfplumber
from docx import Document

def pdf_to_word(pdf_path):
    # Use the same location for the output file
    dir_name = os.path.dirname(pdf_path)
    base_name = os.path.basename(pdf_path)
    name_without_ext = os.path.splitext(base_name)[0]
    doc_path = os.path.join(dir_name, name_without_ext + '.docx')

    # Create a new Word document
    doc = Document()

    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Loop through the pages in the PDF
        for page in pdf.pages:
            # Extract the text from the page
            text = page.extract_text()
            if text:
                # Add the text to the Word document
                doc.add_paragraph(text)

    # Save the Word document
    doc.save(doc_path)

    print(f'The Word document has been saved to: {doc_path}')

if __name__ == "__main__":
    # Ask the user for the PDF file path
    pdf_path = input('Please enter the path of the PDF file: ')
    pdf_to_word(pdf_path)
