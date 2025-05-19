import cv2 as cv
import numpy as np

img = cv.imread('/mnt/01DB783D25219E60/HOMEWORK/TGMT/TH_1/pic.png')
img = img[0:768, 0:1366]
cv.namedWindow('Anh')
h,w = img.shape[:2]
tX = 0

def move_left(pos):
    global tX
    tX = -pos

def move_right(pos):
    global tX
    tX = pos
    

cv.createTrackbar('Trai', 'Anh', 0, w, move_left)
cv.createTrackbar('Phai', 'Anh', 0, w, move_right)


while True:
    M1 = np.float32([[1,0,tX], [0, 1, 0]])
    trans = cv.warpAffine(img, M1, (w, h))
    cv.imshow('Anh', trans)
    if cv.waitKey(1) == ord('q'): 
        break

cv.waitKey(0)
cv.destroyAllWindows()