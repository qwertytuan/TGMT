import cv2
import matplotlib.pyplot as plt
from Anh import Anh

img =cv2.imread(Anh)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgGaussian = cv2.GaussianBlur(imgGray, (3, 3), 0)

laplace= cv2.Laplacian(imgGaussian, cv2.CV_64F, ksize=3)
laplace = cv2.convertScaleAbs(laplace)

canny = cv2.Canny(imgGaussian, 100, 200)

sobelX = cv2.Sobel(imgGaussian,cv2.CV_16S,1,0,ksize=3)
sobelY = cv2.Sobel(imgGaussian,cv2.CV_16S,0,1,ksize=3)
sobelX = cv2.convertScaleAbs(sobelX)
sobelY = cv2.convertScaleAbs(sobelY)
sobel = cv2.addWeighted(sobelX, 0.5, sobelY, 0.5, 0)
# cv2.imshow("sobel", sobel)
# # cv2.imshow("sobelX", sobelX)
# # cv2.imshow("sobelY", sobelY)
# # cv2.imshow("img", img)
# cv2.imshow("Cany", canny)
# cv2.imshow("Laplace", laplace)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
plt.subplot(221)
plt.title("Goc")
plt.axis("off")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)

plt.subplot(222)
plt.title("Sobel")
plt.axis("off")
sobel = cv2.cvtColor(sobel, cv2.COLOR_BGR2RGB)
plt.imshow(sobel)

plt.subplot(223)
plt.title("Canny")
plt.axis("off")
canny = cv2.cvtColor(canny, cv2.COLOR_BGR2RGB)
plt.imshow(canny)

plt.subplot(224)
plt.title("Laplace")
plt.axis("off")
laplace = cv2.cvtColor(laplace, cv2.COLOR_BGR2RGB)
plt.imshow(laplace)
plt.show()




LIM1 = 0
LIM2 = LIM1 * 3

def update_canny(*args):

    global LIM1, LIM2
    LIM1 = cv2.getTrackbarPos("LIM1", "canny")
    LIM2 = LIM1 * 3
    if LIM2 > 255:
        LIM2 = 255
    
    
cv2.namedWindow("canny")
cv2.createTrackbar("LIM1", "canny", 0, 255, update_canny)

while True:
    canny_new = cv2.Canny(imgGaussian, LIM1, LIM2)
    print(LIM1, LIM2)
    cv2.imshow("canny", canny_new)
    if cv2.waitKey(20)== ord("q"):
        break

cv2.destroyAllWindows()



