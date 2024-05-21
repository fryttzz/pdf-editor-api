from fastapi import FastAPI
from routes import pdf

app = FastAPI()

app.include_router(pdf.router, prefix="/pdf")
