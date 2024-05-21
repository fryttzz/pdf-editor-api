from PyPDF2 import PdfWriter
import time
import os

writer = PdfWriter()


def handle(files):
    for file in files:
        if file.endswith(".pdf"):
            writer.append(os.path.join("uploads", file))
            
    filename = f"mergered_{int(time.time())}.pdf"
    mergered_file_path = f"result/{filename}"
    
    writer.write(mergered_file_path)
    writer.close()
    
    return {"path":mergered_file_path, "filename": filename}
