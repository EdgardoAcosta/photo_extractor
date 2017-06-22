from PIL import Image
from PIL import ImageChops
import cv2

im1 = Image.open("cropped_image/cropped_image_0.png")
im2 = Image.open("cropped_image/cropped_image_1.png")
colum = 130
rows = 160
num_images = 20


#cv2.cvtColor(cv2.resize(im1, (colum, rows)) , cv2.COLOR_BGR2RGB)

#num_images
# loop over the image paths
for x in range(0,num_images ):
    read_image = Image.open('cropped_image/cropped_image_'+str(x)+".png")
    #img_prod = cv2.cvtColor(cv2.resize(read_image, (colum, rows)) , cv2.COLOR_BGR2RGB)


    diff = ImageChops.difference(read_image, im1)
    diff.save("out"+str(x)+".png")
print(diff)
