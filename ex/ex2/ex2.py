# • Write a graphical application with OpenCV to:
# 1. read an image from disk
# 2. convert it in grayscale
# 3. show both images on screen

import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_img():
    color = cv2.imread("ex/ex1/image.png", cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY) 

    use_cv = False

    if use_cv:
        # show using cv2
        cv2.imshow("color", color)
        cv2.imshow("gray", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        # show using pyplot (it uses RGB and not BGR)
        color = cv2.cvtColor(color, cv2.COLOR_BGR2RGB) 
        gray = cv2.cvtColor(gray, cv2.COLOR_BGR2RGB) 

        plt.subplot(121)
        plt.title("color")
        plt.imshow(color)
        plt.subplot(122)
        plt.title("gray")
        plt.imshow(gray)
        plt.show()

def main():
    load_img()

if __name__ == "__main__":
    main()