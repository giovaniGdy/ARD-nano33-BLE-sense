from tkinter import filedialog
import shutil
import os

def save_on_directory():

    if os.path.exists("temp/image.jpg"):
        img = "temp/image.jpg"
        path = filedialog.asksaveasfile(mode='w', defaultextension=".jpg", filetypes=(("JPEG (*.JPG)", "*.jpg"),("All Files", "*.*") ))
        if path is None: 
            path.close()
            return
        shutil.move(img, path.name)
    
    path.close()

def import_image():
    img = "temp/image.jpg"
    path = filedialog.askopenfilename()
    
    print(path)
    if path is None: 
        path.close()
        return
    shutil.copy(path, img)