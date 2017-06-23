# import the necessary packages
from scipy.spatial import distance as dist
import matplotlib.pyplot as plt
from matplotlib import pyplot
import numpy as np
import glob
import cv2


# initialize the index dictionary to store the image name
# and corresponding histograms and the images dictionary
# to store the images themselves
index = {}
images = {}
colum = 130
rows = 160
num_images = 20
nbins = 400
bins = np.linspace(0, 1, nbins+1)
#num_images
# loop over the image paths
for x in range(0,num_images):
    read_image = cv2.imread('cropped_image/cropped_image_'+str(x)+".png")
    img_prod = cv2.cvtColor(cv2.resize(read_image, (colum, rows)) , cv2.COLOR_BGR2RGB)
    images["img"+str(x)+".png"] = img_prod

    # the index
    hist = cv2.calcHist([img_prod], [0, 1, 2], None, [8, 8, 8],
                        [0, 256, 0, 256, 0, 256])

    cv2.normalize(hist, hist)
    hist = hist.flatten()
    index["img"+str(x)+".png"] = hist


print(np.digitize(index["img0.png"], bins))

actual_image = "NONE"
best = (( (np.digitize(index["img0.png"], bins) ) > 1).sum())
temp = 0
for (k, hist) in index.items():
    temp = (( (np.digitize(index[k], bins) ) > 1).sum())
    if temp > best:
        best = temp
        actual_image = k

print(actual_image)



plt.subplot(221), plt.imshow(images[actual_image])
plt.subplot(221).axis("off")
plt.subplot(222), plt.plot(index[actual_image], color='g')
plt.show()


"""
# OpenCV methods for histogram comparison
OPENCV_METHODS = (
    ("Correlation", cv2.HISTCMP_CORREL),
    ("Chi-Squared", cv2.HISTCMP_CHISQR),
    ("Intersection", cv2.HISTCMP_INTERSECT),
    ("Hellinger", cv2.HISTCMP_BHATTACHARYYA))

# Loop for methos
for (methodName, method) in OPENCV_METHODS:
  
    results = {}
    reverse = False

    # Correlation or intersection
    if methodName in ("Correlation", "Intersection"):
        reverse = True
        actual_image = 0
        best = ""
        imag2 = ""
        temp = 0
        for (k, hist) in index.items():
            # compute the distance between the two par of histograms
            # in each convination of images
            
            for (j,hist2) in index.items():
                if k != j:
                    d = cv2.compareHist(index[k], hist2, method)
                    if d > temp:
                        #print("image1: " + str(k) + " - image2: " + str(j))
                        imag1 = k
                        imag2 = j
                        temp = d

plt.title("Hist")
plt.subplot(221), plt.imshow(base)
plt.subplot(221).axis("off")
plt.subplot(222), plt.plot(base_hist, color='g')
plt.subplot(223), plt.imshow(images[best])
plt.subplot(223).axis("off")
plt.subplot(224), plt.plot(index[best], color='y')
plt.show()

"""

"""
results[k] = d

        # sort the results
        results = sorted([(v, k) for (k, v) in results.items()], reverse=reverse)
        #print(results)

"""