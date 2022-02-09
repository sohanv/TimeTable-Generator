from PIL import Image
import os.path

def download_button():      # function to save timetable image on desktop
    img = Image.open("tt-new.jpg")

    file_name = "timetable.jpg"
    complete_name = os.path.join(os.path.expanduser('~'),'Desktop', file_name)  # fetches full path for 'Desktop' on any user

    img.save(complete_name)
