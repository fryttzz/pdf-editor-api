from zipfile import ZipFile
from os import path as ospath
import time

def handle(converted):
    zip_name = f"converted_{int(time.time())}.zip"
    path = ospath.join("result", zip_name)

    with ZipFile(path, "w") as myzip:
        for image in converted:
            myzip.write(image)

    return {"path": path, "filename": zip_name}
