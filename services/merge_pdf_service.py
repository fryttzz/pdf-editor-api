from PyPDF2 import PdfWriter
import time
import os

writer = PdfWriter()

def merge_pdfs():
    pdfs_dir = f"{os.curdir}/pdfs"
    for file in os.listdir(pdfs_dir):
        if file.endswith(".pdf"):
            writer.append(os.path.join(pdfs_dir, file))
    writer.write(f"mergered_{int(time.time())}.pdf")
    writer.close()
    print("\nProcesso Finalizado!")