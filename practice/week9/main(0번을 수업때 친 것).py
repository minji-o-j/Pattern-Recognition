import cv2
import numpy as np
import util

filepath= 'retangle.png'
img=cv2.imread(filepath)
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift=cv2.xfeatures2d.SIFT_create() #SIFT 검출기 생성
kpts=sift.detect(image=gray, mask=None) #SIFT 키포인트 검출

res=cv2.drawKeypoints(image=gray, keypoints=kpts, outImage=None)

res_with_rich=cv2.drawKeypoints(image=gray, keypoints=kpts, outImage=None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

concatenated=np.hstack((res,res_with_rich))
cv2.imshow('concatenated',concatenated)
cv2.waitKey(0)