import cv2
import numpy as np
from Anh import Anh

img = cv2.imread(Anh)
cv2.resize(img, None, fx = 8, fy = 8)
cv2.namedWindow("Goc")
h,w = img.shape[:2]

X = 0
def getX(pos):
    global X
    X = pos - w

#Tạo trackbar
cv2.createTrackbar("Dich anh", "Goc", w, w * 2, getX)
while True:
    M1 = np.float32([[1, 0, X], [0, 1, 0]])
    imgNew = cv2.warpAffine(img, M1, (w, h))
    cv2.imshow("Goc", imgNew)
    if cv2.waitKey(20) == ord("q"): break

cv2.destroyAllWindows()