import cv2
import numpy as np
import util
import time

#filepath = 'sky (2).jpg'
filepath = 'bread.jpg'
img = cv2.imread(filepath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()  # SIFT 검출기 생성
surf = cv2.xfeatures2d.SURF_create()  # SURF 검출기 생성

start=0.25
for i in range(5):
    #print(start)
    resize_img=cv2.resize(gray,dsize=((int(gray.shape[0]*start), int(gray.shape[1]*start))))

    print(">> (%d, %d)" %(resize_img.shape[0],resize_img.shape[1]))

    sift_time = time.time()  # SIFT 시작 시간 저장
    kpts = sift.detect(image=gray, mask=None)  # SIFT keypoints 검출
    print("SIFT :", time.time() - sift_time)  # 현재시각 - 시작시간 = 실행 시간

    surf_time = time.time()  # SURF 시작 시간 저장
    kpts = surf.detect(image=gray, mask=None)  # SURF keypoints 검출
    print("SURF :", time.time() - surf_time)  # 현재시각 - 시작시간 = 실행 시간
    print("\n")

    start*=2.0
