from PIL import Image
import os

def png_to_pdf():
    # TODO Fix - only converting one file
    for image in os.listdir(os.curdir + "/images"):
        print(image)
        if image.endswith(".png"):
            converted_dir = r"\converted"
            image_1 = Image.open(f"{os.curdir}/images/{image}")
            im_1 = image_1.convert("RGB")
            im_1.save(os.path.join(f"{os.curdir + converted_dir}", f"{image[:-4]}.pdf"))
    print("\nProcesso Finalizado!")