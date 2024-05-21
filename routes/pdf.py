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


@router.post("/upload_files")
async def upload_files(files: List[UploadFile] = File(...)):

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


@router.post("/upload_file")
async def upload_file(file: UploadFile = File(...)):

    if not allowed_files.handle(file.filename):
        return {"error": "Tipo de arquivo não permitido"}

    content = await file.read()

    save_path = os.path.join("uploads", file.filename)
    with open(save_path, "wb") as f:
        f.write(content)

    return FileResponse(save_path, media_type=file.content_type, filename=file.filename)
