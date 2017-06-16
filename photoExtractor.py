import cv2
import numpy as np

# Import the Classifiers
face_cascade = cv2.CascadeClassifier('HaarCascades/haarcascade_frontalface_default.xml');
eye_cascade = cv2.CascadeClassifier('HaarCascades/haarcascade_eye.xml')
columns = 130
rows = 160
# Load the videocapture
cap = cv2.VideoCapture(0)
# Initialize the counter of images to been taken
counter = 0
while True:
    # Capture an image from the videocam to process it
    ret, img = cap.read()
    # Change it to gray scale in order to apply the HaarCascades
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply the HaarCascades to detect the face
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # For all the different dimentions of faces we find in the image:
    for(x, y, w, h) in faces:
        # Add some values to the face detected in order to cover all the rectangle of the picture in the ID card
        cv2.rectangle(img, (x-30, y-33), (x+w+30, y+h+70), (255, 0, 0), 2) 
        # If the height and width are as expected, and haven't been taken 10 correct photos yet:
        if counter < 10 and h >= 86 and h <= 90 and w >= 86 and w <= 90:
            # Crop the photo of the ID card:
            crop_img = img[y-30:y+h+70,x-28:x+w+29]
            # Apply Haar Cascade to the eyes in the cropped images in gray scale:
            eye_gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
            eyes = eye_cascade.detectMultiScale(eye_gray)
            eyesCounter = 0
            # For each eye found:
            for(ex, ey, ew, eh) in eyes:
                # Increment the counter of eyes
                eyesCounter = eyesCounter + 1;
            # If the number of eyes is equal to (or higher than) 2:
            if eyesCounter >= 2:
                # Save the cropped image and increment the counter
                name = 'cropped_image_' + str(counter)
                crop_img = cv2.resize(crop_img, (columns, rows))
                cv2.imwrite(str(name)+'.png', crop_img)
                counter = counter + 1;
    # Always show what the webcam is seeing, and clase the program when ESC is pressed or when we reach the 10 img cropped:
    cv2.imshow('Webcam Scanner', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27 or counter >= 10:
        break;
# Release the camera and close the windows
cap.release();
cv2.destroyAllWindows()
