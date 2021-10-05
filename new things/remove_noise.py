import cv2
import matplotlib.pyplot as plt

def denoising_img(img, h):
    rm_noise_img = cv2.fastNlMeansDenoisingColored(img, None, h,h,7,21)
    '''
    cv2.fastNlMeansDenoising() – 그레이 이미지 하나에 대해서만 작동함
    cv2.fastNlMeansDenoisingColored() – 칼라 이미지 하나에 대해서 작동함

    위 함수들의 공통 인자는 다음과 같습니다.

    h : 필터 강도를 결정하는 인자. 더 높은 h 값이 잡음을 더 잘 제거하지만 잡음이 아닌 픽셀도 제거함(10이면 적당함)
    hForColorComponents : h와 동일하지만, 칼라 이미지에 대해서만 사용됨(보통 h와 같음)
    templateWindowSize : 홀수값이여야 함(7을 권장함)
    searchWindowSize : 홀수값이여야 함(21을 권장함)
    '''
    return rm_noise_img


if __name__ == "__main__":
    img = cv2.imread('monarija.jpg')
    cv2.imshow("original", img)
    
    for i in range(1,10):
        img = cv2.imread('monarija.jpg')
        dimg = denoising_img(img, 10*i)
        #cv2.imshow(f"remove noise{i}", dimg)
        cv2.imwrite(f'remove noise{i}.png',dimg)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
