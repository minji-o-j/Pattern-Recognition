import cv2
import matplotlib.pyplot as plt

#이미지 import
img=cv2.imread('bread.jpg')

#흑백 변환
gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

#histogram 그리기
plt.hist(gray_img.ravel(),256,[0,256]) #ravel:1차원으로 펴준다
plt.show()
