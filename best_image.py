import numpy as np
import cv2

#Function that return the name of the best image
#This process is made by comparing the histogram of each image
def get_image(num_images):
    #Initialize variables
    index = {} #Array with the histogram of each image
    images = {}#Array with the images
    #Variables to rezies the images
    colum = 130
    rows = 160
    nbins = 400
    bins = np.linspace(0, 1, nbins+1)
    # loop over the image paths
    for x in range(0,num_images):
        #Read image
        read_image = cv2.imread('photos/cropped_image_'+str(x)+".png")
        #Transform to RGB and rezies image to standard
        img_prod = cv2.cvtColor(cv2.resize(read_image, (colum, rows)) , cv2.COLOR_BGR2RGB)
        #Push to array of images
        images["cropped_image_"+str(x)+".png"] = img_prod
        # Calculate histogram
        hist = cv2.calcHist([img_prod], [0, 1, 2], None, [8, 8, 8],
                            [0, 256, 0, 256, 0, 256])
        cv2.normalize(hist, hist)
        hist = hist.flatten()
        #Push to array of histograms
        index["cropped_image_"+str(x)+".png"] = hist
    actual_image = "NONE"
    best = (( (np.digitize(index["cropped_image_0.png"], bins) ) > 1).sum())
    #Iterate the images and histograms
    for (k, hist) in index.items():
        #Get matrix of values of histogram
        temp = (( (np.digitize(index[k], bins) ) > 1).sum())
        if temp > best:
            best = temp
            actual_image = k
    #Return name of best image
    return actual_image