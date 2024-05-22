from PyPDF2 import PdfWriter, PdfReader
import time
import os


def handle(files):
    pdf_writer = PdfWriter()
    for file in files:
        if file.endswith(".pdf"):
            pdf_reader = PdfReader(os.path.join("uploads", file))
            for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    pdf_writer.add_page(page)
    
    filename = f"{os.curdir}/result/merged_{int(time.time())}.pdf"
    print(filename)
    
    with open(filename, "wb") as output_file:
        pdf_writer.write(output_file)

    pdf_writer.close()

    return {"path": filename, "filename": f"merged_{int(time.time())}.pdf"}
