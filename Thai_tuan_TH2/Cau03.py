import cv2
from Anh import Anh

img = cv2.imread(Anh)
print('Kich thuoc anh: ', img.shape[:2])
x = int(input('Nhap kich thuoc x: '))
y = int(input('Nhap kich thuoc y: '))
img2 = cv2.resize(img, (x, y))
cv2.imshow('Anh moi', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
