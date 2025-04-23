import cv2 as cv

cv.namedWindow("Goc")
image = cv.imread('/mnt/01DB783D25219E60/HOMEWORK/TGMT/Thai_tuan_TH3/Anh.jpg')
imageRGB = cv.cvtColor(image, cv.COLOR_BGR2RGB)

xZoom = 1
yZoom = 1
def zoomX(*args):
    global xZoom
    xZoom = cv.getTrackbarPos("ZoomX", "Goc")

    
def zoomY(*args):
    global yZoom
    yZoom = cv.getTrackbarPos("ZoomY", "Goc")
    
cv.createTrackbar("ZoomX", "Goc", 1, 10, zoomX)
cv.createTrackbar("ZoomY", "Goc", 1, 10, zoomY)

while True:
    imageZoom = cv.resize(image, None, fx=xZoom, fy=yZoom, interpolation=cv.INTER_LINEAR)
    
    cv.imshow("Goc", imageZoom)

    key = cv.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('s'):
        cv.imwrite("output.png", imageZoom)

cv.destroyAllWindows()
        