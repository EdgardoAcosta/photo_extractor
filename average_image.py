import cv2
import numpy as np
from PIL import Image
from scipy.misc import toimage
import matplotlib.pyplot as plt

colum = 130
rows = 160
num_images = 20

# Create blank image with height and width as input
#result_image = np.zeros((rows, colum, 3), dtype="float64")
result_image = np.zeros((rows, colum, 3), dtype= np.uint8)


#num_images
for x in range(0,1):
    read_image = cv2.imread('cropped_image/cropped_image_'+str(x)+".png")
    resize_image = np.array(cv2.resize(read_image, (colum, rows)), dtype = np.uint8 )

    vals = resize_image.mean(axis=2).flatten()
    counts, bins = np.histogram(vals, range(257))
    plt.bar(bins[:-1] - 0.5, counts, width=1, edgecolor='none')
    plt.xlim([-0.5, 255.5])
    plt.show()
    #result_image = cv2.add(result_image,resize_image)
    #result_image = cv2.divide(result_image,2)
    #result_image = cv2.multiply(result_image,0.5)


#result_image = cv2.divide(result_image,num_images)
#print(result_image)
#cv2.imwrite("result_image.png", np.uint8(result_image))


