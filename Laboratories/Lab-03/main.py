# import
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Ex 01 (simple cv operations)
def prog_01():
    # load a colored image
    base = cv2.imread("imgs/image.png", cv2.IMREAD_COLOR)
    print(base.shape)

    # convert color base from BGR to RGB
    base_rgb = cv2.cvtColor(base, cv2.COLOR_BGR2RGB)

    # convert color base from BGR to HSV
    base_hsv = cv2.cvtColor(base, cv2.COLOR_BGR2HSV)

    # show all images
    cv2.imshow("SLICE", base[0:200, 0:200])
    cv2.imshow("BGR", base)
    cv2.imshow("RGB", base_rgb)
    cv2.imshow("HSV", base_hsv)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # now change the channel of the main image
    base[:,:,2] = 0     # editing the third channel (0-2)
    cv2.imshow("Channel 0", base)

    base[:, :, 2] = 255 # editing the third channel (0-2)
    cv2.imshow("Channel 255", base)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

####################################################
# Ex 2 (imgs arithmetic operations)
def grab_frame(cap):
    """
    Method to grab a frame from the camera
    :param cap: the VideoCapture object
    :return: the captured image
    """
    ret, frame = cap.read()
    return frame

def handle_close(event, cap):
    """
    Handle the close event of the Matplotlib window by closing the camera capture
    :param event: the close event
    :param cap: the VideoCapture object to be closed
    """
    cap.release()

def bgr_to_gray(image):
    """
    Convert a BGR image into grayscale
    :param image: the BGR image
    :return: the same image but in grayscale
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def prog_02():
    # init the camera
    cap = cv2.VideoCapture(0)

    while cap.isOpened():  # fin tanto che la webcam è aperta definiaimo funzione per acquisire frame
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


####################################################
def main():
    #prog_01()
    prog_02()

if __name__ == "__main__":
    prog_02()