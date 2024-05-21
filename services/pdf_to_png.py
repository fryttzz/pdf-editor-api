from PyPDF2 import PdfWriter
from pdf2image import convert_from_path
from utils import compress_files
import time
import os

writer = PdfWriter()


def handle(file):
    converted = []
    if file.endswith(".pdf"):
        images = convert_from_path(
            file, dpi=300, poppler_path=r"C:\poppler-23.11.0\Library\bin"
        )

        for i in range(len(images)):
            image_name = f"{os.curdir}/result/image_{int(time.time())}.png"
            images[i].save(image_name, "PNG")
            converted.append(image_name)

        zip = compress_files.handle(converted)

    return zip
