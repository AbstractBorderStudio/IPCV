# import
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Ex 01 (simple cv operations)
def prog_01():
    # load a colored image
    base = cv2.imread("Laboratories/Lab-03/imgs/image.png", cv2.IMREAD_COLOR)
    print(base.shape)

    # convert color base from BGR to RGB
    base_rgb = cv2.cvtColor(base, cv2.COLOR_BGR2RGB)

    # convert color base from BGR to HSV
    base_hsv = cv2.cvtColor(base, cv2.COLOR_BGR2HSV)

    # show all images
    # cv2.imshow("SLICE", base[0:200, 0:200])
    # cv2.imshow("BGR", base)
    # cv2.imshow("RGB", base_rgb)
    # cv2.imshow("HSV", base_hsv)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # now change the channel of the main image
    channel_1 = channel_2 = base
    channel_1[:,:,2] = 0     # editing the third channel (0-2)
    channel_2[:, :, 2] = 255 # editing the third channel (0-2)

    fig = plt.figure()
    ax = plt.subplot(1,4,1) 
    ax.imshow(base[0:200, 0:200])
    ax = plt.subplot(1,4,2) 
    ax.imshow(base)
    ax = plt.subplot(1,4,3) 
    ax.imshow(base_rgb)
    ax = plt.subplot(1,4,4) 
    ax.imshow(base_hsv)
    plt.show()

    
    


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

def add_overlay(frame, logo, r, c, i):
    # select a roi
    off = 10
    roi = frame[frame.shape[0]-c-off:frame.shape[0]-off, frame.shape[1]-r-off:frame.shape[1]-off] 
    new = None
    if (i == 0):
        new = logo
    elif (i == 1):
        new = roi - logo
    else:
        new = cv2.addWeighted(logo, 0.3, roi, 0.7, 0.0, new)

    frame[frame.shape[0]-c-off:frame.shape[0]-off, frame.shape[1]-r-off:frame.shape[1]-off] = new
    return frame    

def prog_02():
    # load logo
    logo = cv2.imread("Laboratories\Lab-03\imgs\logo.png", cv2.IMREAD_COLOR)
    logo = cv2.cvtColor(logo, cv2.COLOR_BGR2RGB)
    rows, cols, channels = logo.shape
    
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
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)
        #add_overlay(frame, logo, rows, cols, 0)
        #add_overlay(frame, logo, rows, cols, 1)
        add_overlay(frame, logo, rows, cols, 2)

        if ax_img is None:
            # convert the current (first) frame in grayscale
            ax_img = plt.imshow(frame) #bgr_to_gray(frame), "gray")
            plt.axis("off")  # hide axis, ticks, ...
            plt.title("Camera Capture")
            # show the plot!
            plt.show()
        else:
            # set the current frame as the data to show
            ax_img.set_data(frame) #bgr_to_gray(frame))
            # update the figure associated to the shown plot
            fig.canvas.draw()
            fig.canvas.flush_events()
            plt.pause(1/30)  # pause: 30 frames per second


####################################################
def main():
    #prog_01()
    prog_02()

if __name__ == "__main__":
    main()