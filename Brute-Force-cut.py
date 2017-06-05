import cv2
import numpy as np

# Read source image.
im_src = cv2.imread('template.jpg')
# Four corners of the book in source image
pts_src = np.array([[141, 131], [480, 159], [493, 630], [64, 601]])

# Read destination image.
im_dst = cv2.imread('find.jpg')
# Four corners of the book in destination image.
pts_dst = np.array([[318, 256], [534, 372], [316, 670], [73, 473]])

# Calculate Homography
h, status = cv2.findHomography(pts_src, pts_dst)

# Warp source image to destination based on homography
im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1], im_dst.shape[0]))

# Display images
#cv2.imshow("Warped Source Image", im_out)
cv2.imwrite("Warped-Source-Image.png",im_out)


"""import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('template.jpg',0)          # queryImage
img2 = cv2.imread('find.jpg',0) # trainImage

# Initiate SIFT detector
orb = cv2.ORB_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors.
matches = bf.match(des1,des2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

# Draw first 10 matches.
#img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:20],None, flags=2)

#cv2.imwrite("brute-force.png",img3)


#plt.imshow(img3),plt.show()



# Initialize lists
list_kp1 = []
list_kp2 = []

# For each match...
for mat in matches:

    # Get the matching keypoints for each of the images
    img1_idx = mat.queryIdx
    img2_idx = mat.trainIdx

    # x - columns
    # y - rows
    # Get the coordinates
    (x1,y1) = kp1[img1_idx].pt
    (x2,y2) = kp2[img2_idx].pt

    # Append to each list
    list_kp1.append((x1, y1))
    list_kp2.append((x2, y2))

print(list_kp1)
print("----")
print(list_kp2)
"""
