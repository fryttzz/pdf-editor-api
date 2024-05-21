from typing import List
from fastapi import APIRouter, status, UploadFile, File
from fastapi.responses import FileResponse
from utils import allowed_files
from services import merge as merge_service
import time
import os

router = APIRouter()


@router.get(
    "/", status_code=status.HTTP_200_OK, summary="Retrieves a collection of PDFs"
)
def get_all() -> List:
    return [{"pdf_01": "pdf"}, {"pdf_02": "pdf"}]


@router.post(
    "/merge", status_code=status.HTTP_200_OK, summary="Retorna um PDF mesclado"
)
async def merge(files: List[UploadFile] = File(...)):

    saved_files = []

    for file in files:
        if not allowed_files.handle(file.filename):
            return {"error": "Tipo de arquivo não permitido"}

        content = await file.read()
        new_filename = f"{file.filename[:-4]}_{int(time.time())}.pdf"

        save_path = os.path.join("uploads", new_filename)
        with open(save_path, "wb") as f:
            f.write(content)

        saved_files.append(new_filename)

    merged_file = merge_service.handle(saved_files)

    return FileResponse(merged_file['path'], filename=merged_file['filename'])


@router.post("/split", status_code=status.HTTP_200_OK, summary="Retorna os PDF separados")
async def split(file: UploadFile = File(...)):
    if not allowed_files.handle(file.filename):
        return {"error": "Tipo de arquivo não permitido"}

    content = await file.read()

    save_path = os.path.join("uploads", file.filename)
    with open(save_path, "wb") as f:
        f.write(content)

    return FileResponse(save_path, media_type=file.content_type, filename=file.filename)


@router.post("/pdf_to_png", status_code=status.HTTP_200_OK, summary="Transforma um PDF em PNG")
async def pdf_to_png(file: UploadFile = File(...)):
    pass


@router.post("/png_to_pdf", status_code=status.HTTP_200_OK, summary="Transforma um PNG em PDF")
async def png_to_pdf(file: UploadFile = File(...)):
    pass
