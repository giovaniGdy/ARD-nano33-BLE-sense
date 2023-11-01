import numpy as np
import cv2

def convertSave():
    with open("data.txt") as file:
        data = file.read()
        buff = bytes.fromhex(data)

    # Convert to 3 channel uint8 numpy array representing the BGR image
    img = cv2.cvtColor(
        np.frombuffer(buff, dtype=np.uint8).reshape(240, 320, 2), cv2.COLOR_BGR5652BGR
    )

    # Save the image to a png file
    cv2.imwrite("image.png", img)
