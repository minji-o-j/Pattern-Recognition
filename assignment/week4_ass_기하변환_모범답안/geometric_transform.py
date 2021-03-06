import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(17, 5))

img = cv2.imread('hand.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
height = img.shape[0]
width = img.shape[1]
plt.subplot(1, 3, 1) #1행 3열로 나누고 그중 첫번째
plt.imshow(img)
plt.axis('off')
plt.title('original')


# OpenCV를 이용한 변환 행렬 도출
center = (width / 2, height / 2)
cv_M = cv2.getRotationMatrix2D(center, 90, 1.0)  # 회전 방향이 반시계방향(CCW; Counter Clock-Wise)
cv_result = cv2.warpAffine(img, cv_M, (width, height))
print('>> OpenCV Rotation matrix')
print(cv_M, end='\n\n')

plt.subplot(1, 3, 2)
plt.imshow(cv_result)
plt.axis('off')
plt.title('cv_result')

# 직접 도출한 행렬을 이용한 회전 변환 - 행렬 조함 이용(matmul,행렬곱)
##과제
fwd_tran_M = np.array([[1, 0, -center[0]],
                       [0, 1, -center[1]],
                       [0, 0, 1]])


rot_M= np.array([[0,1,0],
                 [-1,0,0],
                 [0,0,1]])

bwd_tran_M = np.array([[1, 0, center[0]],
                       [0, 1, center[1]],
                       [0, 0, 1]])

# - 단일 변환행렬 생성
tmp=np.matmul(rot_M,fwd_tran_M)
my_M=np.matmul(bwd_tran_M,tmp)
my_M=my_M[0:2, 0:3]
#print(np.delete(my_M, 2, axis = 0))
##
print('>> My matrix')
print(my_M)
my_result = cv2.warpAffine(img, my_M, (width, height))

plt.subplot(1, 3, 3)
plt.imshow(my_result)
plt.axis('off')
plt.title('my_result')

# figure 출력
plt.tight_layout()
plt.show()
