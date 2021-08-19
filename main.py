import ai
import faceDetector
if __name__ == "__main__":

    fileName = input("파일 경로를 입력하시오: ")
    try:
        face_image,eye1,eye2,nose,mouth=faceDetector.detect(fileName)
        
        ai.score([eye1,eye2,nose,mouth])
    except faceDetector.readError:
        print("Image read Error")
    except faceDetector.noFaceException:
        print("no Face Detected.")
    except faceDetector.noEyesException:
        print("no Eyes Detected.")