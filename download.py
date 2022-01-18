from PIL import Image
import os.path

def download_button():
    img = Image.open("tt-new.jpg")

    file_name = "timetable.jpg"
    complete_name = os.path.join(os.path.expanduser('~'),'Desktop', file_name)

    img.save(complete_name)

download_button()