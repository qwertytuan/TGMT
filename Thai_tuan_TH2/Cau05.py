import cv2
import numpy as np
from Anh import Anh

img = cv2.imread(Anh)
h,w = img.shape[:2]
x = float(input('Nhap goc xoay x: '))
M = cv2.getRotationMatrix2D((0,0), x, 1)
img_new = cv2.warpAffine(img, M, (w,h))
cv2.imshow('Anh', img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()