import cv2, numpy as np
 

def preprocess():
    image=cv2.imread('img.jpg',cv2.IMREAD_COLOR)
    if image is None : return None, None
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    return image,gray

face_cascade = cv2.CascadeClassifier("haar/haarcascade_frontalface_alt2.xml")
eye_cascade = cv2.CascadeClassifier("haar/haarcascade_eye.xml")
image,gray=preprocess()

if image is None : raise Exception("read error")

faces = face_cascade.detectMultiScale(gray,1.1,2,0,(100,100))

if faces.any():
    print(faces[0])
    x,y,w,h=faces[0]
    face_image = image[y:y+h,x:x+w]
    eyes = eye_cascade.detectMultiScale(face_image)
    
    if len(eyes) == 2:
        for ex,ey,ew,eh in eyes:
            center= (x+ex+ew//2, y+ey+eh//2)
            cv2.circle(image,center,10,(0,255,0),2)

    else:
        print("눈이 없음")

    cv2.rectangle(image,faces[0],(255,0,0),2)
    image = cv2.resize(image, dsize=(600,600),interpolation=cv2.INTER_LINEAR)
    cv2.imshow("yeah",image)

else:
    print("얼굴이 없음")

cv2.waitKey()
