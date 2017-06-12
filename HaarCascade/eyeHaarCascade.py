import cv2
import numpy as np

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml');
img = cv2.imread('cropped_image_9.png')

while True:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray)
    for(ex, ey, ew, eh) in eyes:
        cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)
        print("ex: ", ex)
        print("ey: ", ey)
        print("eh: ", eh)
        print("ew: ", ew)
        '''
        print("W: ", w)
        print("H: ", h)
        print("\n")
        
        # Probaré cortando la imagen ahora:
        
        if counter < 20 and h >= 83 and h <= 90 and w >= 83 and w <= 90:
            crop_img = img[y-30:y+h+45,x-20:x+w+20]
            name = 'cropped_image_' + str(counter)
            cv2.imwrite(str(name)+'.png', crop_img)
            counter = counter + 1;
        
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for(ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        '''
    cv2.imshow('Webcam Scanner', img)
    cv2.waitKey(0)
    break

cv2.destroyAllWindows()
