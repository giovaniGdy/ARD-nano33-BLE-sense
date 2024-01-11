import numpy as np
import cv2

def convertSave():
    with open("temp/data.txt") as file:
        data = file.read()
        buff = bytes.fromhex(data)

    img = cv2.cvtColor(
        np.frombuffer(buff, dtype=np.uint8).reshape(240, 320, 2), cv2.COLOR_BGR5652BGR
    )

    cv2.imwrite("temp/image.png", img)
