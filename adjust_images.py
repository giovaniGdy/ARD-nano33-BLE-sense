import cv2
from PIL import Image

def adjust_images():
    image = Image.open('image.png')
    new_image = image.resize((640, 480))
    new_image.save('image.jpg')
