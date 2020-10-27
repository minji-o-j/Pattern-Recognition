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
    edge_img = cv2.Canny(blur_img, 70, 140)

    # 4) 관심 영역(ROI; Region Of Interest)을 설정하여 배경 영역 제외 (차선 이외 edge 정보 날리기 위해)
    ROI_img=set_region_of_interest(edge_img,vertices)

    # 5) 허프 변환을 사용하여 조건을 만족하는 직선 검출
    line_vertex=cv2.HoughLinesP(ROI_img,    # image
                                1,          # rho: r값의 범위 - 0~1 실수
                                np.pi/180,  # theta: 𝜃값의 범위 - 0~180 정수
                                20,         # threshold: Hough Space에서 만나는 교차점의 기준 - 숫자가 작으면 많은 선 검출, 숫자가 크면 정확도가 높아짐
                                10,         # minLineLength: 선의 최소길이
                                3)          # maxLineGap: 점의 사이 거리가 이 값보다 크면 다른 선으로 간주, 숫자 작아질수록 len(line_vertex) 커짐
    
    # 6) 찾은 직선들을 입력 이미지에 그리기
    ## print(line_vertex)  # [[[744 480 745 481]] [[790 498 791 499]] ...] 3차원 배열 형태
    ## print(len(line_vertex))
    ## result=cv2.line(ROI_img,tuple(line_vertex[0][0]),tuple(line_vertex[1][0]),(0,0,255))
    ### > TypeError: function takes exactly 2 arguments (4 given) # [744 480 745 481] 이렇게 들어가서 시작점, 끝점 나눠줘야 함


    result=np.copy(img) #원본 위에 선 그리기 위해 원본 복사
    for i in range(0,len(line_vertex)):
        #print(line_vertex[i])  ## [[659 417 662 419]] 이런 형태
        #print('+++++++++')
        for x1, y1, x2, y2 in line_vertex[i]: # [[]] 형태가 아니라 []이면 TypeError: cannot unpack non-iterable numpy.intc object 발생
            cv2.line(result,            # img: 선을 그릴 이미지
                     (x1,y1), (x2,y2),  # pt1, pt2: x1,y1 -> (x1, y1), tuple형태로 바꿔줌
                     (0,0,255),         # color: BGR순서, (0,0,255)->빨간색
                     3)                 # thickness
    '''
    for line in line_vertex:
        print(line)
        print('+++++++++')
        for x1, y1, x2, y2 in line:
            cv2.line(result, (x1, y1), (x2, y2), (0, 0, 255), 3)
    '''

    return result

    # 변수 설명, 코드 참고: https://opencv-python.readthedocs.io/en/latest/doc/25.imageHoughLineTransform/imageHoughLineTransform.html
    # 변수 설명 참고: https://m.blog.naver.com/windowsub0406/220894462409