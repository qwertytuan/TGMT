import cv2
from Anh import Anh

img = cv2.imread(Anh)
cv2.imshow("Goc", img)
h,w=img.shape[:2]

print("Chieu cao:", h)
print("Chieu rong:", w)

b, g, r = img[200, 100] 
print(f"Giá trị màu tại toạ độ [100,200]: B={b}, G = {g}, R = {r}")

x1 = int(input("Nhap x1: "))
y1 = int(input("Nhap y1: "))
x2 = int(input("Nhap x2: "))
y2 = int(input("Nhap y2: "))

imgCrop = img[y1: y2, x1: x2]

cv2.imshow("Crop", imgCrop)

cv2.waitKey(0)
cv2.destroyAllWindows()
