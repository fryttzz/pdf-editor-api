from typing import List
from fastapi import APIRouter, status, UploadFile, File
from fastapi.responses import FileResponse
from utils import allowed_files
import os

router = APIRouter()


@router.get(
    "/", status_code=status.HTTP_200_OK, summary="Retrieves a collection of PDFs"
)
def get_all() -> List:
    return [{"pdf_01": "pdf"}, {"pdf_02": "pdf"}]


@router.post("/merge")
async def merge(files: List[UploadFile] = File(...)):

    saved_files = []

    for file in files:
        if not allowed_files.handle(file.filename):
            return {"error": "Tipo de arquivo não permitido"}

        content = await file.read()

        save_path = os.path.join("uploads", file.filename)
        with open(save_path, "wb") as f:
            f.write(content)

        saved_files.append(save_path)

    return {"files": saved_files}


@router.post("/split")
async def split(file: UploadFile = File(...)):
    if not allowed_files.handle(file.filename):
        return {"error": "Tipo de arquivo não permitido"}

    content = await file.read()

    save_path = os.path.join("uploads", file.filename)
    with open(save_path, "wb") as f:
        f.write(content)

    return FileResponse(save_path, media_type=file.content_type, filename=file.filename)


@router.post("/pdf_to_png")
async def pdf_to_png(file: UploadFile = File(...)):
    pass

@router.post("/png_to_pdf")
async def png_to_pdf(file: UploadFile = File(...)):
    pass