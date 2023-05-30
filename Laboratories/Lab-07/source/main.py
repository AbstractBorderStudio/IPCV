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

def detect_faces(frame, cls):
    """
    Method to detect faces in the current frame
    :frame: current frame
    :cls: classifier
    """
    #min_size = np.array()
    
    f = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    faces = cls.detectMultiScale(frame, minSize = [200, 200])

    for face in faces:
        cv2.rectangle(f, (face[0],face[1]), (face[0]+face[2],face[1]+face[3]), (255,0,0), 3)

    return f

def gray_equalize(frame):
    """
    Method to convert image into grayscale and
    equalize it's histogram.
    :frame: current frame
    """
    return cv2.equalizeHist(bgr_to_gray(frame))
    

def capture(cls):
    """
    Method to capture a grayscale image
    from the main camera and recognise
    faces
    :cls: pre-loaded classifier
    """
    
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
        
        # turn frame grayscale and equalize histogram
        g_eq_frame = gray_equalize(frame)

        # detect faces
        rec_frame = detect_faces(g_eq_frame, cls)

        if ax_img is None:
            # convert the current (first) frame in grayscale
            ax_img = plt.imshow(rec_frame, "gray")
            plt.axis("off")  # hide axis, ticks, ...
            plt.title("Camera Capture")
            # show the plot!
            plt.show()
        else:
            # set the current frame as the data to show
            ax_img.set_data(rec_frame)
            # update the figure associated to the shown plot
            fig.canvas.draw()
            fig.canvas.flush_events()
            plt.pause(1/30)  # pause: 30 frames per second


def load_classifier(mode):
    """
    Method to load a main classifier
    from a path, if not it loads the 
    :cv2: default classifier
    """
    if (mode == 0):
        return cv2.CascadeClassifier('Laboratories/Lab-07/materiale/haarcascades/haarcascade_frontalface_default.xml')
    elif (mode == 1):
        return cv2.CascadeClassifier('Laboratories/Lab-07/materiale/lbpcascades/lbpcascade_frontalface.xml')
    else:
        return None
    

def main():
    cls = load_classifier(1)
    if not cls:
        print("unable to load classifier")
        return
    capture(cls)

if __name__ == "__main__":
    main()