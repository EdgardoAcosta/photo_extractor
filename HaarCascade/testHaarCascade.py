import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml');

cap = cv2.VideoCapture(0)

counter = 0
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for(x, y, w, h) in faces:
        # Entre 59 y 65 es el rango de h y w para cortar
        cv2.rectangle(img, (x-30, y-33), (x+w+30, y+h+70), (255, 0, 0), 2) 
        '''
        print("W: ", w)
        print("H: ", h)
        print("\n")
        '''
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
    cv2.imshow('Webcam Scanner', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27 or counter >= 20:
        break;

cap.release();
cv2.destroyAllWindows()
