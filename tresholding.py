import cv2
import numpy as np
import matplotlib
import imutils


img = cv2.imread('example.jpg',0) #pass 0 to convert into gray level
ret,thr =cv2.threshold(img,0,255,cv2.THRESH_OTSU)
img1 = cv2.medianBlur(img,9)
th3 = cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)



resized = imutils.resize(img, width=300)
ratio = img.shape[0] / float(resized.shape[0])
blurred = cv2.GaussianBlur(resized, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)



cv2.imwrite("shape.jpg",cnts)
cv2.imwrite("image.jpg",thr)
cv2.imwrite("adatative.jpg",th3)

