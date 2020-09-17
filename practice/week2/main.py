import cv2

img=cv2.imread('bread.jpg')

cv2.imshow('image',img)
cv2.waitKey() #특정 키를 누르기 전까지 안꺼지게 한다