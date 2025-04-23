import cv2
from Anh import Anh

img = cv2.imread(Anh)
cv2.namedWindow('Anh')
h,w = img.shape[:2]
tX = 0

def get_rotate(pos):
    global tX
    tX = pos

cv2.createTrackbar('Xoay', 'Anh', 0, 360, get_rotate)
while True:
    M = cv2.getRotationMatrix2D((w / 2, h / 2), -tX, 0.8)
    img_new = cv2.warpAffine(img, M, (w,h))
    cv2.imshow('Anh', img_new)
    if cv2.waitKey(20) == ord('q'): break

cv2.waitKey(0)
cv2.destroyAllWindows()