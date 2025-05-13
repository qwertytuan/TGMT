import cv2 as cv

image = cv.imread('pic.png')
image = cv.resize(image, (600, 400))
image_blur = cv.GaussianBlur(image, (3, 3), 0)

image_gray=cv.cvtColor(image_blur, cv.COLOR_BGR2GRAY)
LIM1=100
LIM2=LIM1+100
def update_lim(*args):
    global LIM1
    LIM1 = cv.getTrackbarPos("LIM", "Binary")

cv.namedWindow("Binary")
cv.createTrackbar("LIM", "Binary", 100, 255, update_lim)

while True:
    ret,imgbinary=cv.threshold(image_gray, LIM1, LIM2 , cv.THRESH_BINARY)
    cv.imshow("Binary", imgbinary)
    if cv.waitKey(1)== ord("q"):
        break