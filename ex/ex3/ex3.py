# - Write a graphical application with OpenCV to:
# 1. acquire the video stream from the webcam
# 2. convert it in grayscale
# 3. show the result of the acquisition on screen

import cv2
import numpy as np
import matplotlib.pyplot as plt

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

def capture():
    # init the camera
    cap = cv2.VideoCapture(0)

    # enable Matplotlib interactive mode
    plt.ion()

    # create a figure to be updated
    fig = plt.figure()
    fig.canvas.mpl_connect("close_event", lambda event: handle_close(event, cap))

    # prep a variable for the first run
    ax_img = None

    while cap.isOpened():
        # get the current frame
        frame = grab_frame(cap)
        frame = cv2.flip(frame, 1)

        if ax_img is None:
            # convert the current (first) frame in grayscale
            ax_img = plt.imshow(bgr_to_gray(frame))
            plt.axis("off")  # hide axis, ticks, ...
            plt.title("Camera Capture")
            # show the plot!
            plt.show()
        else:
            # set the current frame as the data to show
            ax_img.set_data(bgr_to_gray(frame))
            # update the figure associated to the shown plot
            fig.canvas.draw()
            fig.canvas.flush_events()
            plt.pause(1/30)  # pause: 30 frames per second

def main():
    capture()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)