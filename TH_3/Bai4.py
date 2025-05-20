import cv2 as cv

image = cv.imread('TH_3/bai1.jpg')
image= cv.resize(image, (1366, 768))
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

image_bilateral = cv.bilateralFilter(image_gray, 9, 75, 75)
_,image_binary = cv.threshold(image_bilateral, 100, 150, cv.THRESH_BINARY)

contur,_= cv.findContours(image_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for c in contur:
    image = cv.drawContours(image, [c], -1, (255, 0, 0), 2)
 


cv.imshow('Bilateral Filter', image)

cv.waitKey(0)
cv.destroyAllWindows()
