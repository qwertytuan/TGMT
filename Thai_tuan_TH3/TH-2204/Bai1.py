# from Anh import Anh
import cv2 as cv
import matplotlib.pyplot as plt

image= cv.imread('/mnt/01DB783D25219E60/HOMEWORK/TGMT/Thai_tuan_TH3/Anh.jpg')
imageRGB = cv.cvtColor(image, cv.COLOR_BGR2RGB)

w = int(input("Width: "))
h = int(input("Height: "))
LeftropCordsX = int(input("Crop cords X: "))
LeftropCordsY = int(input("Crop cords Y: "))

 
imageCrop = imageRGB[LeftropCordsY:LeftropCordsY+h, LeftropCordsX:LeftropCordsX+w]

imageGauss=cv.GaussianBlur(imageCrop, (5, 5), 0)

imageGray=cv.cvtColor(imageGauss, cv.COLOR_BGR2GRAY)

AdaptiveThreshold = cv.adaptiveThreshold(imageGray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)


plt.subplot(221)
plt.title("Goc")
plt.axis("off")
plt.imshow(imageRGB)

plt.subplot(222)
plt.title("Crop")
plt.axis("off")
plt.imshow(imageCrop)

plt.subplot(223)
plt.title("Gauss")
plt.axis("off")
plt.imshow(imageGauss)

plt.subplot(224)
plt.title("Adaptive")
plt.axis("off")
plt.imshow(AdaptiveThreshold, cmap='gray')

plt.savefig('TH-2204/output.png')

cv.waitKey(0)
cv.destroyAllWindows()
