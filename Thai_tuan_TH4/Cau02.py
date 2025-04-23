
import cv2 as cv
from AnhTh4 import Anh

image = cv.imread(Anh)
image_rgb= cv.cvtColor(image, cv.COLOR_BGR2RGB)
image_gray = cv.cvtColor(image_rgb, cv.COLOR_RGB2GRAY)

kernel = 1

def kernel_size(*args):
    global kernel
    kernel = int(cv.getTrackbarPos('Kernel', 'Goc'))
    if kernel % 2 == 0:
        kernel += 1
    elif kernel == 0:
        kernel = 1
    
    
cv.namedWindow('Goc')
cv.createTrackbar('Kernel', 'Goc', 1, 20, kernel_size)

while True:
    median= cv.medianBlur(image_gray, kernel)
    cv.imshow('Goc', median)
    if cv.waitKey(ord('q'))== ord('q'):
        
        break
    elif cv.waitKey(ord('s'))== ord('s'):
        cv.imwrite('/Thai_tuan_TH4/Cau02.png', median)
        break
    else:
        pass
cv.waitKey(0)
cv.destroyAllWindows()

