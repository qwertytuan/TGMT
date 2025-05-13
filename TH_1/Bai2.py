import cv2 as cv

image = cv.imread('pic.png')
image = cv.resize(image, (600, 400))
center = (image.shape[1] // 2, image.shape[0] // 2)
angle = 0

def Rotate(*args):
    global angle
    angle = 0 - cv.getTrackbarPos("Angle", "Rotate")
    
cv.namedWindow("Rotate")
cv.createTrackbar("Angle", "Rotate", 0, 360, Rotate)

while True:
    M=cv.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv.warpAffine(image, M, (image.shape[1], image.shape[0]))
    cv.imshow("Rotate", rotated)
    if cv.waitKey(1) == ord('q'):
        break
    
cv.waitKey(0)
cv.destroyAllWindows()
