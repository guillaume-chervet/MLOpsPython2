from io import BytesIO
from pathlib import Path
import fitz
from fitz import Document, Pixmap

def convert_pixmap_to_rgb(pixmap) -> Pixmap:
    """Convert to rgb in order to write on png"""
    # check if it is already on rgb
    if pixmap.n < 4:
        return pixmap
    else:
        return fitz.Pixmap(fitz.csRGB, pixmap)

def extract_images_from_pdf(pdfs_directory_path:str, images_directory_path:str):
    Path(images_directory_path).mkdir(parents=True, exist_ok=True)
    files = [p for p in Path(pdfs_directory_path).iterdir() if p.is_file()]
    for path in files:
        with open(path, "rb") as file_stream:
            with fitz.open(stream=file_stream.read(), filetype="pdf") as document_stream:
                file_images = []
                number_pages = len(document_stream) - 1
                for i in range(number_pages):
                    page = document_stream[i]
                    images = document_stream.get_page_images(i)
                    nunber_images = len(images)
                    for j, image in enumerate(images):
                        xref = image[0]
                        pix = fitz.Pixmap(document_stream, xref)
                        bytes = BytesIO(convert_pixmap_to_rgb(pix).tobytes())
                        filename = path.stem + "_page" + str(i) + "_index" + str(j) + ".png"
                        path_filename = "{0}\\{1}".format(images_directory_path, filename)
                        file_images.append(filename)
                        with open(path_filename, "wb") as f:
                            f.write(bytes.getbuffer())
                return file_images


#pdfs_directory_path = ".\dataset-cats-dogs-others"
#images_directory_path = ".\extracted_images"


#extract_images_from_pdf(pdfs_directory_path, images_directory_path)