import cv2

cap = cv2.VideoCapture(0)


while True:
    ret,img = cap.read()
    cv2.imshow('you',img)
    if cv2.waitKey(20)==32:
        cv2.imwrite("img.jpg",img)
    