import cv2
import pipeline
img = cv2.imread('./data/test_images/solidWhiteRight.jpg')
result = pipeline.run(img)

cv2.imshow('result', result)
cv2.waitKey(0)
#cv2.imwrite('result.png',result)

cv2.destroyAllWindows() #창이 모두 꺼지도록 정리

'''
# 동영상 테스트
cap = cv2.VideoCapture('./data/test_videos/solidWhiteRight.mp4')

while True:
    ok, frame = cap.read()
    if not ok:
        break

    result = pipeline.run(frame)

    cv2.imshow('result', result)
    key = cv2.waitKey(1)  # -1
    if key == ord('x'):
        break
cap.release()
cv2.destroyAllWindows()
'''
'''
# 동영상 저장--- http://blog.naver.com/PostView.nhn?blogId=rhrkdfus&logNo=221401081261&from=search&redirect=Log&widgetTypeCall=true&directAccess=false
cap = cv2.VideoCapture('./data/test_videos/solidWhiteRight.mp4')
## 재생할 파일의 넓이와 높이
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (int(width), int(height)))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        print("종료")
        break;

    result = pipeline.run(frame)

    cv2.imshow('result', result)
    out.write(result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()
#---
'''

