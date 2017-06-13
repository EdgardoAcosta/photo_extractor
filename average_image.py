import cv2
import numpy as np

colum = 130
rows = 160
num_images = 20

# Create blank image with height and width as input
result_image = np.zeros((rows, colum, 3), np.uint8)


#num_images
for x in range(0,num_images):
    print("image: " + str(x))
    read_image = cv2.imread('cropped_image/cropped_image_'+str(x)+".png")
    resize_image = cv2.resize(read_image, (colum, rows))


    result_image = cv2.add(result_image,resize_image)
    #result_image = cv2.divide(result_image,2)
    result_image = cv2.multiply(result_image,0.5)


cv2.imwrite("result_image.png",result_image)