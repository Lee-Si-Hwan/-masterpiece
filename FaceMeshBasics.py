import cv2
import mediapipe as mp

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=3)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=3, color=(255,255,255))

img=cv2.imread("test.jpg")
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
results = faceMesh.process(imgRGB)

if results.multi_face_landmarks:
    
    for faceLandmark in results.multi_face_landmarks:
        
        mpDraw.draw_landmarks(img, faceLandmark, mpFaceMesh.FACE_CONNECTIONS,
                          drawSpec,drawSpec)
        
    for id,lm in enumerate(faceLandmark.landmark):
        ih, iw, ic = img.shape
        x,y = int(lm.x*iw), int(lm.y*ih)
img=cv2.resize(img,dsize=(600,600),interpolation=cv2.INTER_LINEAR);
cv2.imshow("RESULT!!!!!", img)
cv2.imwrite("result.jpg",img)
cv2.waitKey(0)
