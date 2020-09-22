import cv2
import matplotlib.pyplot as plt

#이미지 import
img=cv2.imread('bread.jpg')

#흑백 변환
gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

#histogram 그리기
hist=cv2.calcHist(gray_img,[0],None,[256],[0,256])

'''
cv2.calcHist(images,channels,mask,histSize,ranges [,hist[,accumulate]])
1. images: 분석할 이미지 "리스트" [img]
2. channels: 분석할 채널, 1채널이면 [0], 3채널이면 [0](blue), [1](green), [0,2](blue, red)의 형태
3. mask: 분석할 이미지 영역 마스크, None이면 전체 영역
4. histSize: bin(x축 칸의 개수)의 개수 [256], 채널 2차원 ([0,2]와 같은)인 경우 [256,256] 이런식
'''

plt.plot(hist)
plt.show()
