import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "Laboratories/Lab-04/"

def ex1():
    img = cv2.imread(path + "sinFunction.png", cv2.IMREAD_GRAYSCALE)
    apply_tdf(img)
    show(img)

def apply_tdf(img):
    tmp = cv2.dft(img, flags=cv2.DFT_COMPLEX_OUTPUT)

def show(img):
    cv2.imshow("window", img)
    cv2.waitKey(0)
    cv2.deleteAllWindows()

def main():
    ex1()

if __name__ == "__main__":
    main()