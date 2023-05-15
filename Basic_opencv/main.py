# we'll be using these libraries
import cv2 as cv
import numpy as np
import matplotlib as mpl

# on pycharm the path is relative to the file and not the project
path = "imgs/circle.png"

# drawing
# generate a 512x512 matrix with all zeros which is a black image 
image = np.zeros((512, 512, 3), np.uint8)
identity = np.eye(512)


# draw a circle on the image just created
radius = int(512/4)
thickness = 1
pos = int(512/2)
color = (0,0,255) # red

image = cv.circle(image, (pos, pos), radius, color ,thickness)

# Save image to disk
cv.imwrite(path, image)

# Load the image we just saved
circle = cv.imread(path, -1)     #(flag = 0 or 1 or -1)

pos_top = (int(512/2 - 512/4), int(512/2 - 512/4))
pos_bot = (int(512/2 + 512/4), int(512/2 + 512/4))
circle_square = cv.rectangle(circle,pos_top,pos_bot,color,thickness)                   #Color is by default black

circle_square_rgb = cv.cvtColor(circle_square, cv.COLOR_RGB2BGR)

b = circle_square_rgb[:,:,1]


# Show the image in a window
cv.imshow("Window Name", b)
cv.waitKey(0)
cv.destroyAllWindows()

