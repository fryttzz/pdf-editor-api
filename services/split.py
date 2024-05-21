from PyPDF2 import PdfReader, PdfWriter
import os

writer = PdfWriter()

def pdf_split():
    pdfs_dir = os.curdir

    for file in os.listdir(pdfs_dir):
        if file.endswith(".pdf"):
            print(file)
            pdf = PdfReader(file)

            for page in range(len(pdf.pages)):
                writer.add_page(pdf.pages[page])
                output_filename = "{}/pdfs/{}_page_{}.pdf".format(
                    os.curdir, file[:-4], page + 1
                )

                with open(output_filename, "wb") as out:
                    writer.write(out)
                writer.close()

                print("Created: {}".format(output_filename))
    print("\nProcesso Finalizado!")