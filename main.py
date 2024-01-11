import tkinter
from tkinter import *
from PIL import Image, ImageTk
import PIL.Image
import sys

sys.path.insert(1, './test_functions/')

from save_on_location import *
from arduino_connector import *
from convert_and_save import *
from adjust_images import *
from image_recognition import *


class App(Frame):

    dropdown_selection_prediction = "MobileNetV2 - Fastest prediction / Moderate Accuracy"
    
    def capture(self):
        takePicture()

        convertSave()
        adjust_images()

        img = ImageTk.PhotoImage(Image.open('temp/image.jpg'))
        self.label1.configure(image=img)
        self.label1.image = img
        
    def importing_image(self):
        import_image()
        
        img = ImageTk.PhotoImage(Image.open('temp/image.jpg'))
        self.label1.configure(image=img)
        self.label1.image = img

    def prediction(self):
        dsp = self.dropdown_selection_prediction
        dsp = dsp.split()[0]
        
        if os.path.exists("temp/image.jpg"):
            predict(dsp)
            
            with open("temp/prediction_data.txt") as file:
                data = file.read()

            self.text_box.config(state='normal')
            self.text_box.delete('1.0', END)
            self.text_box.insert('end', data)
            self.text_box.config(state='disable')
        
            os.remove("temp/prediction_data.txt")
        else:
            self.text_box.config(state='normal')
            self.text_box.insert('end', "\nNo image found.")
            self.text_box.config(state='disable')
    
    def widgets(self):
        img = ImageTk.PhotoImage(PIL.Image.open("default/cam_default.jpg"))
        self.label = Label(root, width=100, font=("Arial", 10),
                           text="Arduino Nano 33 BLE Sense Lite w/ OV7576 Camera")
        self.label.pack(fill="x")

        self.label1 = tkinter.Label(image=img, width=640, height=480)
        self.label1.image = img
        self.label1.place(x=25, y=45)

        self.button = Button(root, command=self.capture, width=44, font=(
            "Arial", 15), text="Take Picture").place(x=690, y=45)

        self.button = Button(root, command=save_on_directory, width=44, font=(
            "Arial", 15), text="Save").place(x=690, y=100)
        
        self.button = Button(root, command=self.importing_image, width=44, font=(
            "Arial", 15), text="Import Image").place(x=690, y=155)
        
        dropdown_options = ["MobileNetV2 - Fastest prediction / Moderate Accuracy", 
                            "InceptionV3 - Slow prediction / Higher Accuracy", 
                            "DenseNet121 - Slower prediction / Highest Accuracy"]
        default_option = StringVar(root)
        default_option.set(dropdown_options[0])
        
        def dropdown_selection(selection):
            self.dropdown_selection_prediction = selection
            
        self.dropdown = OptionMenu(root, default_option, *dropdown_options, command=dropdown_selection)
        self.dropdown.config(width=74)
        self.dropdown.place(x=690, y=310)
        
        self.button = Button(root, command=self.prediction, width=44, font=(
            "Arial", 15), text="IA Prediction").place(x=690, y=260)

        self.text_box = Text(root, height=10, width=54, font=(
            "Arial", 12))
        self.text_box.insert('end', "")
        self.text_box.config(state='disabled')
        self.text_box.place(x=690, y=345)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.widgets()


root = Tk()
root.title("Camera Capture")
root.configure(background="gray")
root.resizable(False, False)
root.geometry("1200x600")


def exit_application():
    if os.path.exists("temp/image.jpg"):
        os.remove("temp/image.jpg")

    if os.path.exists("temp/image.png"):
        os.remove("temp/image.png")
        os.remove("temp/data.txt")

    if os.path.exists("temp/prediction_data.txt"):
        os.remove("temp/prediction_data.txt")
        
    root.destroy()


root.protocol("WM_DELETE_WINDOW", exit_application)

app = App(master=root)
app.mainloop()
