from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class UploadFileRequest(BaseModel):
    name: str
    file_path: str

@app.post("/uploads.new")
def new_upload(request: UploadFileRequest):
    """Process the upload request coming.

    Gets the input image and detects the faces from the image. stores image & face images in storage and updates the DB.
    """
    return {
        "ok": True
    }

@app.get("/images.list")
def list_images():
    """Lists all the images.
    """
    return {
        "ok": True,
        "images": []
    }

@app.get("/images.get")
def get_image(id: str):
    """Returns the main image and processed face images.
    """
    return {
        "ok": True
    }