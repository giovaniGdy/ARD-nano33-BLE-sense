import tkinter
from tkinter import *
from PIL import Image, ImageTk

from arduino_connector import *
from convert_and_save import *
from adjust_images import *
from save_on_location import *


def capture():

    takePicture()

    convertSave()

    adjust_images()

    img = ImageTk.PhotoImage(Image.open('image.jpg'))
    label1.configure(image=img)
    label1.image = img


def teste():
    print("aaaa")


root = Tk()
root.title("Camera Capture")
root.configure(background="gray")
root.resizable(False, False)
root.geometry("1200x600")
label = Label(root, width=100, font=("Arial", 10),
              text="Arduino Nano 33 BLE Sense Lite w/ OV7576 Camera")
label.pack(fill="x")


img = ImageTk.PhotoImage(Image.open("cam_default.jpg"))
label1 = tkinter.Label(image=img, width=640, height=480)
label1.image = img
label1.place(x=25, y=45)

Button(root, command=capture, width=44, font=(
    "Arial", 15), text="Take Picture").place(x=690, y=45)
Button(root, command=save_on_directory, width=44, font=(
    "Arial", 15), text="Save").place(x=690, y=100)

root.mainloop()
