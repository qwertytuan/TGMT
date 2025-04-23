# import cv2 as cv

# img=cv.imread("/home/tuan/Downloads/Telegram Desktop/CV/Bai_thuc_hanh_1/Example.jpg")

# def get_dosang(pos):
#     global dosang
#     dosang = pos

# def get_tuongphang(pos):
#     global tuongphang
#     tuongphang = pos/10

# def get_default(state, userdata):
#     global dosang, tuongphang
#     dosang = 0
#     tuongphang = 1
#     cv.setTrackbarPos('Alpha', 'Trackbar', 10)
#     cv.setTrackbarPos('Beta', 'Trackbar', 10)

# dosang = 0
# tuongphang = 1

# cv.namedWindow('Trackbar')
# cv.createTrackbar('Alpha', 'Trackbar', 10, 30, get_dosang)
# cv.createTrackbar('Beta', 'Trackbar', 10, 100, get_tuongphang)
# cv.createButton('Default', get_default)
# while True:
#     new = cv.convertScaleAbs(img, alpha=tuongphang, beta=dosang)
#     cv.imshow('Trackbar', new)
#     if cv.waitKey(10)== ord('q'):
#         break
    
# cv.destroyAllWindows()


# import cv2 as cv
# import numpy as np
# img=cv.imread("/home/tuan/Downloads/Telegram Desktop/CV/Bai_thuc_hanh_1/Example.jpg")
# h,w=img.shape[:2]
# tx,ty=-100,-150
# M=np.float32([[1,0,tx],[0,1,ty]])
# result=cv.warpAffine(img,M,(w,h))
# rotate=cv.getRotationMatrix2D((w/2,h/2),45,1)
# cv.imshow("ban dau",img)
# cv.imshow("ket qua",result)
# cv.imshow("rotate",cv.warpAffine(img,rotate,(w,h)))
# cv.waitKey(0)
# cv.destroyAllWindows()

import cv2
import numpy as np

img = cv2.imread("/home/tuan/Downloads/Telegram Desktop/CV/Bai_thuc_hanh_1/Example.jpg")
def getAngle(pos):
    global angle
    angle = pos

tx = 0
ty = 0
def getMovePosx(posx):
    tx = posx

def getMovePosy(posy):
    ty = posy

cv2.namedWindow('Trackbar')
cv2.createTrackbar('Angle', 'Trackbar', 0, 360, getAngle)
cv2.createTrackbar("moveX", 'Trackbar', -100, 100, getMovePosx)
cv2.setTrackbarPos("moveX", 'Trackbar', 0)
cv2.createTrackbar("moveY", 'Trackbar', -100, 100, getMovePosy)
cv2.setTrackbarPos("moveY", 'Trackbar', 0)
while True:
    h, w = img.shape[:2]
    angle = cv2.getTrackbarPos('Angle', 'Trackbar')
    Movex= cv2.getTrackbarPos('moveX', 'Trackbar')
    Movey = cv2.getTrackbarPos('moveY', 'Trackbar')
    rotate = cv2.getRotationMatrix2D((w/2, h/2), angle, 1)
    result = cv2.warpAffine(img, rotate, (w, h))
    M = np.float32([[1, 0, Movex], [0, 1, Movey]])
    result2 = cv2.warpAffine(result, M, (w, h))
    cv2.imshow('Trackbar', result2)
    if cv2.waitKey(10)== ord('q'):
        break

    
    
cv2.destroyAllWindows()