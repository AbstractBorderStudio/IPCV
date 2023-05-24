import cv2
import numpy as np
import matplotlib.pyplot as plt

# set img path
path = "Laboratories/Lab-03/imgs/image.png"

# create figure (manipulate window size)
fig = plt.figure(figsize=(15,5))

# load img
im = cv2.imread(path, cv2.IMREAD_COLOR)
# convert to rgb
im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# equalize
eq_img = cv2.equalizeHist(img)

# calc histo
hist = cv2.calcHist([img],[0],None,[256],[0,256])
eq_hist = cv2.calcHist([eq_img],[0],None,[256],[0,256])

img_g_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
eq_img_g_rgb = cv2.cvtColor(eq_img, cv2.COLOR_BGR2RGB)


# add subplot
fig.add_subplot(2,3,1)
plt.imshow(img_g_rgb)
plt.axis("off")
plt.title("img")

fig.add_subplot(2,3,2)
plt.plot(hist)
plt.title("cv2")

fig.add_subplot(2,3,3)
plt.hist(img.ravel(),256,[0,256])
plt.title("plt")

fig.add_subplot(2,3,4)
plt.imshow(eq_img_g_rgb)
plt.title("eq cv2")

fig.add_subplot(2,3,5)
plt.plot(eq_hist)
plt.title("cv2")

fig.add_subplot(2,3,6)
plt.hist(eq_img.ravel(),256,[0,256])
plt.title("plt")

plt.show()