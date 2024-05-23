from typing import List
from fastapi import APIRouter, status, UploadFile, File
from fastapi.responses import FileResponse
from utils import allowed_files
from services import merge as merge_service
from services import pdf_to_png as pdf_to_png_service
from services import png_to_pdf as png_to_pdf_service
from services import split as split_service
import time
import os

router = APIRouter()


@router.post(
    "/merge", status_code=status.HTTP_200_OK, summary="Retorna um PDF mesclado"
)
async def merge(files: List[UploadFile] = File(...)):

    saved_files = []

    for file in files:
        if not allowed_files.handle(file.filename):
            return {"error": "Tipo de arquivo não permitido"}

        content = await file.read()
        new_filename = f"{int(time.time())}_{file.filename}"

        save_path = os.path.join("uploads", new_filename)
        with open(save_path, "wb") as f:
            f.write(content)

        saved_files.append(new_filename)

    merged_file = merge_service.handle(saved_files)

    return FileResponse(merged_file["path"], filename=merged_file["filename"])


@router.post(
    "/split", status_code=status.HTTP_200_OK, summary="Retorna os PDF separados"
)
async def split(file: UploadFile = File(...)):
    if not allowed_files.handle(file.filename):
        return {"error": "Tipo de arquivo não permitido"}

    content = await file.read()

    save_path = os.path.join("uploads", file.filename)
    with open(save_path, "wb") as f:
        f.write(content)

    converted_file = split_service.handle(save_path)

    return FileResponse(converted_file["path"], filename=converted_file["filename"])


@router.post(
    "/pdf_to_png", status_code=status.HTTP_200_OK, summary="Transforma um PDF em PNG"
)
async def pdf_to_png(file: UploadFile = File(...)):

    if not allowed_files.handle(file.filename):
        return {"error": "Tipo de arquivo não permitido"}

    content = await file.read()
    new_filename = f"{int(time.time())}_{file.filename}"

    save_path = os.path.join("uploads", new_filename)
    with open(save_path, "wb") as f:
        f.write(content)

    converted_file = pdf_to_png_service.handle(save_path)

    return FileResponse(converted_file["path"], filename=converted_file["filename"])


@router.post(
    "/png_to_pdf", status_code=status.HTTP_200_OK, summary="Transforma um PNG em PDF"
)
async def png_to_pdf(file: UploadFile = File(...)):
    if not allowed_files.handle(file.filename):
        return {"error": "Tipo de arquivo não permitido"}

    content = await file.read()
    new_filename = f"{int(time.time())}_{file.filename}"

    save_path = os.path.join("uploads", new_filename)
    with open(save_path, "wb") as f:
        f.write(content)

    converted_file = png_to_pdf_service.handle(save_path)

    return FileResponse(converted_file["path"], filename=converted_file["filename"])
