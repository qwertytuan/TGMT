import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from Anh import Anh

img = cv.imread(Anh)
imgColor = cv.cvtColor(img, cv.COLOR_BGR2RGB)

imgblur = cv.GaussianBlur(img, (3, 3), 0)

imggray=cv.cvtColor(imgblur, cv.COLOR_BGR2GRAY)

ret1,th1=cv.threshold(imggray,127,255,cv.THRESH_BINARY)

th2 = cv.adaptiveThreshold(imggray,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2)

ret2,th3=cv.threshold(imggray,127,255,cv.THRESH_BINARY+cv.THRESH_OTSU)


imges=[imgColor,th1,th2,th3]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(imges[i])
    plt.title('Image'+str(i+1))
    plt.axis('off')
    plt.set_cmap('gray')
plt.show() 



LIM=0
def update_lim(*args):
    global LIM
    LIM = cv.getTrackbarPos("LIM", "Binary")

cv.namedWindow("Binary")
cv.createTrackbar("LIM", "Binary", 0, 255, update_lim)

while True:
    ret3,imgbinary=cv.threshold(imggray, LIM, 255, cv.THRESH_BINARY)
    cv.imshow("Binary", imgbinary)
    if cv.waitKey(20)== ord("q"):
        break

cv.destroyAllWindows()