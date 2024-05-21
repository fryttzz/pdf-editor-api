ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "pdf"}


def handle(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
