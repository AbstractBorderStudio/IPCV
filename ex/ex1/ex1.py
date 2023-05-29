# • Write a simple OpenCV program to:
# 1. create and print a 3x3 identity matrix
# 2. read an image from disk
# 3. convert the image in grayscale
# 4. save title grayscale image back on disk

import cv2
import numpy as np
import matplotlib.pyplot as plt

def identity_mat(n):
    eye = np.eye(n)
    print(eye)

def load_img():
    img = cv2.imread("ex/ex1/image.png", cv2.IMREAD_COLOR)
    g_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    cv2.imwrite("ex/ex1/image_g.png", g_img)

def main():
    identity_mat(3)
    load_img()

if __name__ == "__main__":
    main()