from fastapi import FastAPI
from routes import pdf
import uvicorn

app = FastAPI()

app.include_router(pdf.router, prefix="/pdf")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True)
