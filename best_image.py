import numpy as np
import cv2


def get_image():
    # initialize the index dictionary to store the image name
    # and corresponding histograms and the images dictionary
    # to store the images themselves
    index = {}
    images = {}
    colum = 130
    rows = 160
    num_images = 10
    nbins = 400
    bins = np.linspace(0, 1, nbins+1)
    #num_images
    # loop over the image paths
    for x in range(0,num_images):
        read_image = cv2.imread('photos/cropped_image_'+str(x)+".png")
        img_prod = cv2.cvtColor(cv2.resize(read_image, (colum, rows)) , cv2.COLOR_BGR2RGB)
        #Array of images
        images["cropped_image_"+str(x)+".png"] = img_prod
        # Calculate histogram
        hist = cv2.calcHist([img_prod], [0, 1, 2], None, [8, 8, 8],
                            [0, 256, 0, 256, 0, 256])

        cv2.normalize(hist, hist)
        hist = hist.flatten()
        #Array of histograms
        index["cropped_image_"+str(x)+".png"] = hist


    #print(np.digitize(index["img0.png"], bins))

    actual_image = "NONE"
    best = (( (np.digitize(index["cropped_image_0.png"], bins) ) > 1).sum())
    temp = 0
    for (k, hist) in index.items():
        temp = (( (np.digitize(index[k], bins) ) > 1).sum())
        if temp > best:
            best = temp
            actual_image = k

    return actual_image
