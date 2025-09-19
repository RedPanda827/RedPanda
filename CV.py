import cv2

img = cv2.imread('sea.jpg', 1)

cv2.imshow('TEST', img) # 분수가 보이면 overroading이 된 이름이 같은 함수가 분모이다.

cv2.waitKey(0) # 아무키를 누르면 윈도우를 종료시켜라 라는 의미
cv2.destroyAllWindows()
# 로컬에서 진행시 필요한 코드
