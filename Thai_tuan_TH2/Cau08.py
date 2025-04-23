import cv2
import numpy as np
from Anh import Anh

img = cv2.imread(Anh)
cv2.namedWindow('Anh')
h,w = img.shape[:2]
tX = 0
tY = 0


def move_left(pos):
    global tX
    tX = -pos

def move_right(pos):
    global tX
    tX = pos
    
def move_up(pos):
    global tY
    tY = -pos
    
def move_down(pos):
    global tY
    tY = pos

cv2.createTrackbar('Trai', 'Anh', 0, 100, move_left)
cv2.createTrackbar('Phai', 'Anh', 0, 100, move_right)
cv2.createTrackbar('Tren', 'Anh', 0, 100, move_up)
cv2.createTrackbar('Duoi', 'Anh', 0, 100, move_down)



while True:
    M1 = np.float32([[1,0,tX], [0, 1, tY]])
    trans = cv2.warpAffine(img, M1, (w, h))
    cv2.imshow('Anh', trans)
    if cv2.waitKey(20) == ord('q'): break

cv2.waitKey(0)
cv2.destroyAllWindows()