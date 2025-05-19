import cv2 as cv
import numpy as np

image = cv.imread('/mnt/01DB783D25219E60/HOMEWORK/TGMT/TH_1/pic.png')
image = cv.resize(image, (1366, 768))

image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
image_blur = cv.GaussianBlur(image_gray, (3, 3), 0)

canny = cv.Canny(image_gray,0,200)
contours, _ = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

image_contours = image.copy()
cv.drawContours(image_contours, contours, -1, (0, 255, 0), 1)
cv.imshow("contours", image_contours)
cv.imshow("canny", canny)
cv.waitKey(0)
cv.destroyAllWindows()
    