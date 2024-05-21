from PyPDF2 import PdfWriter
from pdf2image import convert_from_path
import os

writer = PdfWriter()

def pdf_to_png():
    for pdf in os.listdir(os.curdir):
        if pdf.endswith(".pdf"):
            images = convert_from_path(pdf,dpi=300, poppler_path=r"C:\poppler-23.11.0\Library\bin")

            for i in range(len(images)):
                images[i].save(os.curdir + '/images/page_'+ str(i) +'.png', 'PNG')
    print("\nProcesso Finalizado!")
