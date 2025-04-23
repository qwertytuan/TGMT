# Đọc ảnh, 
# vẽ contour của ảnh bằng màu đỏ.
# Lưu lại ảnh sau khi vẽ contour. 

import cv2 as cv
from AnhTh4 import Anh
import numpy as np

image = cv.imread(Anh)


image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
image_gray = cv.blur(image_gray, (3,3))

canny_output = cv.Canny(image_gray,100, 200)
contours, _ = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


image_out = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8) 

for i in range(len(contours)):
    color = (255,0,0)
    cv.drawContours(image_out, contours, i, color, 2)
    
cv.imshow('Original',cv.cvtColor(image, cv.COLOR_BGR2RGB))
cv.imshow('Contours', cv.cvtColor(image_out, cv.COLOR_BGR2RGB))
cv.waitKey(0)
cv.destroyAllWindows()