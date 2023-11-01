from tkinter import filedialog
import shutil
import os

def save_on_directory():
    path = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")

    if path is None: 
        return
    img = "./image.jpg"
    shutil.move(img, path.name)
    path.close()
    os.remove(img)
