import cv2

def pipeline(img):
    # img=cv2.imread('./data/test_images/solidWhiteRight.jpg')

    #edge는 gray영상에서 찾겠다
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    blurred_img=cv2.GaussianBlur(gray_img,(15,15),0.0)

    edge_img=cv2.Canny(blurred_img, 70,140)

    #cv2.imshow('edge',edge_img)
    #cv2.waitKey()

    return edge_img


cap=cv2.VideoCapture('./data/test_videos/solidWhiteRight.mp4')

while True:
    ok,frame=cap.read()

    if not ok:
        break  #끝까지 읽었을 때 종료

    edge_img=pipeline(frame)

    cv2.imshow('edge',edge_img)

    #cv2.waitKey() #버튼 하나를 눌러야지 동영상이 나온다.
    #cv2.waitKey(1000)  # 1초마다 프레임을 읽는다.
    key=cv2.waitKey(30) # 아무 키 입려도 받지 않았으면 -1

    if key==ord('x'): #x를 누를시 종료
        break

cap.release() #동영상 다 썼으면