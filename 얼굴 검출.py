import cv2, numpy as np
from face_utils import *


face_cascade = cv2.CascadeClassifier("haar/haarcascade_frontalface_alt2.xml")
eye_cascade = cv2.CascadeClassifier("haar/haarcascade_eye.xml")
image,gray=preprocess()

if image is None : raise Exception("read error")

faces = face_cascade.detectMultiScale(gray,1.1,2,0,(100,100))

if faces.any():
    print(faces[0])
    x,y,w,h=faces[0]
    face_image = image[y:y+h,x:x+w]
    eyes = eye_cascade.detectMultiScale(face_image,1.15,7,0,(25,20))
    
    if len(eyes) == 2:
        face_center=(x+w//2,y+h//2)
        face_center_f=(float(x+w//2),float(y+h//2))
        eye_centers=[(x+ex+ew//2,y+ey+eh//2) for ex,ey,ew,eh in eyes]
        corr_image, corr_center = correct_image(image,face_center_f,eye_centers)
        rois=detect_object(face_center,faces[0])
        print(2)
        cv2.rectangle(corr_image,rois[0],(255,0,255),2)
        cv2.rectangle(corr_image,rois[1],(255,0,255),2)
        cv2.rectangle(corr_image,rois[2],(255,0,0),2)
        print(corr_center[0])
        print(corr_center[1])
        print(face_center)
        cv2.circle(corr_image,tuple(corr_center[0]),5,(0,255,0),2)
        cv2.circle(corr_image,tuple(corr_center[1]),5,(0,255,0),2)
        cv2.circle(corr_image,face_center,3,(0,0,255),2)

        cv2.imshow("yeeee",corr_image)
        print(1)
    else:
        print("눈이 없음")

    cv2.rectangle(image,faces[0],(255,0,0),2)
    # image = cv2.resize(image, dsize=(600,600),interpolation=cv2.INTER_LINEAR)
    cv2.imshow("yeah",image)

else:
    print("얼굴이 없음")

cv2.waitKey()