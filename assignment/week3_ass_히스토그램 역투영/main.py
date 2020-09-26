import cv2
import numpy as np

# 모델 영상의 2차원 H-S 히스토그램 계산
img_m=cv2.imread('model.jpg')
hsv_m=cv2.cvtColor(img_m,cv2.COLOR_BGR2HSV)
hist_m=cv2.calcHist([hsv_m],[0,1],None,[180,256],[0,180,0,256])

# 입력 영상의 2차원 H-S 히스토그램 계산
img_i=cv2.imread('hand.jpg')
hsv_i=cv2.cvtColor(img_i, cv2.COLOR_BGR2HSV)
hist_i=cv2.calcHist([hsv_i],[0,1],None,[180,256],[0,180,0,256])

# 히스토그램 정규화
##과제
height_m, width_m = img_m.shape[0], img_m.shape[1]
height_i, width_i = img_i.shape[0], img_i.shape[1]
hist_m =hist_m/(height_m*width_m)
hist_i =hist_i/(height_i*width_i)
##
print("maximum of hist_m: %f" %hist_m.max()) #값 범위 체크 :1.0 이하
print("maximum of hist_i: %f" %hist_i.max()) #값 범위 체크 :1.0 이하

# 비율 히스토그램 계산
##과제
hist_r=np.zeros((180,256))
#print(hist_m.shape)
#print(hist_i.shape)
#print(hist_r.shape)
for j in range(180):
    for i in range(256):
        hist_r[j,i] = min((hist_m[j,i]/(hist_i[j,i]+0.00000001)), 1.0)
print(hist_r.shape)
##
print("range of hist_r: [%.1f, %.1f]"%(hist_r.min(),hist_r.max())) # 비율 값 범위 체크

# 히스토그램 역투영 수행
##과제

h,s,v=cv2.split(hsv_i)
result=np.zeros((height_i,width_i))
print(result.shape)
print(h.shape)
print(s.shape)
for i in range(width_i):
    for j in range(height_i):
        result[j,i]=hist_r[h[j,i],s[j,i]]
 ##

# 이진화 수행 (화소값이 임계값 0.02보다 크면 255, 그렇지 않으면 0)
ret, thresholded=cv2.threshold(result, 0.02, 255, cv2.THRESH_BINARY)
cv2.imwrite('result.jpg', thresholded)

# 모폴로지 연산 적용
##과제
kernel=np.ones((13,13),np.uint8)
improved=cv2.morphologyEx(thresholded,cv2.MORPH_CLOSE,kernel)
##
cv2.imwrite('morphology_close_13(2).jpg',improved)