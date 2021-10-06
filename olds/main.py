import ai
import faceDetector

successedFile=list()
resultCoordinates=list()
noFaceList=list()
noEyesList=list()
if __name__ == "__main__":
    #range(ord('a'),ord('n')+1)
    fileName = input("파일 경로를 입력하시오: ")
    
    try:
        face_image,eye1,eye2,nose,mouth,imgWidth,imgHeight=faceDetector.detect(fileName)
            
        data=ai.score([eye1,eye2,nose,mouth])
        resultCoordinates.append(data)
        successedFile.append(fileName)
    except faceDetector.readError:
        print("Image read Error")
    except faceDetector.noFaceException:
        print("no Face Detected. Please Specify the area of face.")
        noFaceList.append(fileName)
    except faceDetector.noEyesException:
        print("no Eyes Detected.")
        noEyesList.append(fileName)
    print(successedFile)
    print(resultCoordinates)
    print(noFaceList)
    print(noEyesList)
