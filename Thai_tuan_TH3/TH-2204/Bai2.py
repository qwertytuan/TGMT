import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread('/mnt/01DB783D25219E60/HOMEWORK/TGMT/Thai_tuan_TH3/Anh.jpg')
imageRGB = cv.cvtColor(image, cv.COLOR_BGR2RGB)
imageGauss = cv.GaussianBlur(imageRGB, (5, 5), 0)
imageGray = cv.cvtColor(imageGauss, cv.COLOR_BGR2GRAY)
# binary threshold
LIM1 = int(input("LIM1: "))
LIM2 = int(input("LIM2: "))
if LIM1 < 0 or LIM1 > 255:
    print("LIM1 must be in range [0, 255]")
    exit(1)
elif LIM1 > LIM2:
    print("LIM1 must be less than LIM2")
    exit(1)
else:
    ret, binary = cv.threshold(imageGray, LIM1, LIM2, cv.THRESH_BINARY)
    
kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))

closing = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)

opening = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)

sobelX = cv.Sobel(imageGray,cv.CV_16S,1,0,ksize=3)
sobelY = cv.Sobel(imageGray,cv.CV_16S,0,1,ksize=3)
sobelX = cv.convertScaleAbs(sobelX)
sobelY = cv.convertScaleAbs(sobelY)
sobel = cv.addWeighted(sobelX, 0.5, sobelY, 0.5, 0)

plt.subplot(231)
plt.title("Goc")
plt.axis("off")
plt.imshow(imageRGB)

plt.subplot(232)
plt.title("sobel")
plt.axis("off")
plt.imshow(sobel,cmap='gray')

plt.subplot(233)
plt.title("Binary")
plt.axis("off")
plt.imshow(binary, cmap='gray')

plt.subplot(234)
plt.title("Open")
plt.axis("off")
plt.imshow(opening,cmap='gray')

plt.subplot(235)
plt.title("Close")
plt.axis("off")
plt.imshow(closing,cmap='gray')

plt.savefig('TH-2204/output.png')

cv.imshow("Goc", cv.cvtColor(imageRGB, cv.COLOR_RGB2BGR))
cv.imshow("sobel", sobel)
cv.imshow("Binary", binary)
cv.imshow("Open", opening)
cv.imshow("Close", closing)

if cv.waitKey(20) == ord('q') or cv.waitKey(20)== ord('Esc'):
    plt.savefig('TH-2204/output.png')
    print("Saved")
    cv.destroyAllWindows()
cv.waitKey(0)
cv.destroyAllWindows()