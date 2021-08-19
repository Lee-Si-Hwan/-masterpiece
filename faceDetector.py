import cv2, numpy as np
from faceUtils import *

class readError(Exception):
    pass
class detectError(Exception):
    pass
class noFaceException(detectError):
    pass
class noEyesException(detectError):
    pass

face_cascade = cv2.CascadeClassifier("haar/haarcascade_frontalface_alt2.xml")
eye_cascade = cv2.CascadeClassifier("haar/haarcascade_eye.xml")

def detect(imgName):
    image,gray=loadImage(imgName)

    if image is None : raise readError("read error")

    faces = face_cascade.detectMultiScale(gray,1.1,2,0,(100,100))
    try:
        if faces.any():
            print(faces[0])
            x,y,w,h=faces[0]
            face_image = image[y:y+h,x:x+w]
            eyes = eye_cascade.detectMultiScale(face_image,1.15,7,0,(25,20))
            
            if len(eyes) == 2:
                face_center=(x+w//2,y+h//2)
                face_center_f=(float(x+w//2),float(y+h//2))
                eye_centers=[(x+ex+ew//2,y+ey+eh//2) for ex,ey,ew,eh in eyes]
                corr_image, corr_center = correctImage(image,face_center_f,eye_centers)
                rois=detectObject(face_center,faces[0])
                print(2)
                # cv2.rectangle(corr_image,rois[0],(255,0,255),2)
                # cv2.rectangle(corr_image,rois[1],(255,0,255),2)
                cv2.rectangle(corr_image,rois[2],(255,0,0),2)
                print(corr_center[0]) # 눈 1
                print(corr_center[1]) # 눈 2
                print(face_center)
                cv2.circle(corr_image,tuple(corr_center[0]),5,(0,255,0),2)
                cv2.circle(corr_image,tuple(corr_center[1]),5,(0,255,0),2)
                cv2.circle(corr_image,face_center,3,(0,0,255),2)

                cv2.imshow("yeeee",corr_image)
                cv2.rectangle(image,faces[0],(255,0,0),2)
                
                resizedImage = cv2.resize(image, dsize=(600,600),interpolation=cv2.INTER_LINEAR)
                cv2.imshow("yeah",image)
                return resizedImage,list(corr_center[0]),list(corr_center[1]),list(face_center),list(rois[2])
            
            else:
                raise noEyesException("no Eye")
    except AttributeError:
        raise noFaceException("no Face")