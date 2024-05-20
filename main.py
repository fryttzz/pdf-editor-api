from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import os

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "pdf"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    if not allowed_file(file.filename):
        return {"error": "Tipo de arquivo não permitido"}

    content = await file.read()

    save_path = os.path.join("uploads", file.filename)
    with open(save_path, "wb") as f:
        f.write(content)

    return FileResponse(save_path, media_type=file.content_type, filename=file.filename)
