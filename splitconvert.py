import cv2
import numpy as np


# opencv uses B,G,R
img = cv2.imread("image.jpg")

# split color image into 3 separate channels
b,g,r = cv2.split(img)

# converts BGR to HSV color model
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h,s,v = cv2.split(img_hsv)

#increase saturation
s[:] = 255

#merge channels
img_saturated = cv2.merge((h,s,v))

#convert back to RGB
img_satrgb = cv2.cvtColor(img_saturated, cv2.COLOR_HSV2BGR)

cv2.imshow("input", img)
cv2.imshow("saturated", img_satrgb)
cv2.waitKey(0)

