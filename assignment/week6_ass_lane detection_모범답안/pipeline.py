import numpy as np
import cv2


def set_region_of_interest(img, vertices): #관심 영역 설정
    """

    :param img:       대상 이미지
    :param vertices:  이미지에서 남기고자 하는 영역의 꼭짓점 좌표 리스트
    :return:
    관심 영역만 마스킹 된 이미지
    """

    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)

    return cv2.bitwise_and(img, mask)


def run(img):
    height, width = img.shape[:2]

    #관심 영역 꼭짓점 설정하는 부분
    vertices = np.array([[(50, height),
                          (width // 2 - 45, height // 2 + 60),
                          (width // 2 + 45, height // 2 + 60),
                          (width - 50, height)]])


    # 1) BGR -> GRAY 영상으로 색 변환
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    # 2) 이미지 내 노이즈를 완화시키기 위해 blur 효과 적용
    blur_img = cv2.GaussianBlur(gray_img, (7, 7), 0)


    # 3) 캐니 엣지 검출을 사용하여 엣지 영상 검출
    edge_img = cv2.Canny(blur_img,
                         threshold1=70,
                         threshold2=175)

    # 4) 관심 영역(ROI; Region Of Interest)을 설정하여 배경 영역 제외 (차선 이외 edge 정보 날리기 위해)
    ROI_img=set_region_of_interest(edge_img,vertices)

    # ROI->edge를 할 경우 ROI 자르는 부분까지 선으로 고려(사다리꼴로..)

    # 5) 허프 변환을 사용하여 조건을 만족하는 직선 검출
    line_vertex=cv2.HoughLinesP(ROI_img,         # image
                                rho=1,           # 거리 해상도(pixel)
                                theta=np.pi/180, # 각도 해상도(radian)
                                threshold=10,    # 변환 공간에서 만나야 하는 점의 기준(기준이 작으면
                                minLineLength=15,# minLineLength보다 작으면 직선으로 검출하지 않음
                                maxLineGap=40)   # maxLineGap보다 크면 서로 다른 직선으로 판단
    # 6) 찾은 직선들을 입력 이미지에 그리기

    result=np.copy(img)

    for line in line_vertex:
        print(line)
        for x1, y1, x2, y2 in line:
            cv2.line(result, (x1, y1), (x2, y2), (0, 0, 255), 5) #BGR, 굵기

    return result