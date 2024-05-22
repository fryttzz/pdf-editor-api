from PyPDF2 import PdfReader, PdfWriter
from utils import compress_files
import time
import os

def handle(file):
    writer = PdfWriter()
    splited_files = []

    if file.endswith(".pdf"):
        pdf = PdfReader(file)

        for page in range(len(pdf.pages)):
            writer.add_page(pdf.pages[page])
            output_filename = f"{os.curdir}/result/{int(time.time())}_page_{page + 1}.pdf"
            splited_files.append(f"{os.curdir}/result/{int(time.time())}_page_{page + 1}.pdf")

            with open(output_filename, "wb") as out:
                writer.write(out)
            writer.close()

        zip = compress_files.handle(splited_files)
    return zip