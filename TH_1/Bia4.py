import cv2 as cv
import numpy as np

image = cv.imread('pic.png')
image = cv.resize(image, (600, 400))

image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

def median_blur(*args):
    global kernel_size
    kernel_size = cv.getTrackbarPos("Kernel Size", "Median Blur")
    if kernel_size % 2 == 0:
        kernel_size += 1
        
cv.namedWindow("Median Blur")
kernel_size = 1
cv.createTrackbar("Kernel Size", "Median Blur", 1, 20, median_blur)


while True:
    image_blur = cv.medianBlur(image, kernel_size)
    image_blur_gray = cv.cvtColor(image_blur, cv.COLOR_BGR2GRAY)
    binary_output = cv.threshold(image_blur_gray, 100, 200, cv.THRESH_BINARY)[1]
    contours, _ = cv.findContours(binary_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    image_contours = image_blur.copy()
    if cv.waitKey(1) == ord('q'):
        break
    
    if cv.waitKey(1) == ord('c'):
        cv.drawContours(image_contours, contours, -1, (0, 255, 0), 2)
        if cv.waitKey(1) == ord('s'):
            cv.imwrite('contours.png', image_contours)
        
    if cv.waitKey(1) == ord('s'):
        cv.imwrite('contours.png', image_contours)
    cv.imshow("Median Blur", image_contours)
    
cv.waitKey(0)
cv.destroyAllWindows()
    