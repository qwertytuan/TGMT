import cv2 as cv
import numpy as np

img = cv.imread('TH_3/bai1.jpg')
img = img[0:768, 0:1366]
cv.namedWindow('Anh')
h,w = img.shape[:2]
tY = 0

def move_down(pos):
    global tY
    tY = -pos

def move_up(pos):
    global tY
    tY = pos
    

cv.createTrackbar('Len', 'Anh', 0, h, move_down)
cv.createTrackbar('Xuong', 'Anh', 0, h, move_up)


while True:
    M1 = np.float32([[1,0,0], [0, 1, tY]])
    trans = cv.warpAffine(img, M1, (w, h))
    cv.imshow('Anh', trans)
    if cv.waitKey(1) == ord('q'): 
        break

cv.waitKey(0)
cv.destroyAllWindows()