from PIL import Image
import time
import os


def handle(file):
    if file.endswith(".png") or file.endswith(".jpg"):
        image = Image.open(f"{os.curdir}/{file}")
        im = image.convert("RGB")
        new_path = f"{os.curdir}/result/converted_{int(time.time())}.pdf"
        im.save(new_path)

    return {"path": new_path, "filename": f"converted_{int(time.time())}.pdf"}
