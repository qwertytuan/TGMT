import cv2
from Anh import Anh

img = cv2.imread(Anh)

x = float(input("Nhap vao kich thuoc x: "))
y = float(input("Nhap vao kich thuoc y: "))

imgNew = cv2.resize(img, None, fx = x, fy= y)

cv2.imshow("Goc", img)
cv2.imshow("New", imgNew)

cv2.waitKey(0)
cv2.destroyAllWindows()
