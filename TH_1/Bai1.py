import cv2 as cv

def DilationAndErosion(img):
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    _, img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)
    img_dilation = cv.dilate(img_binary, kernel)
    img_erosion = cv.erode(img_binary, kernel)
    return img_dilation, img_erosion


video = cv.VideoCapture('Thai_tuan_TH4/Video.mp4')

while True:
    ret, frame = video.read()
    if not ret:
        break
    cv.imshow("Video", frame)
    
    if cv.waitKey(1) == ord("s"):
        dilation, erosion = DilationAndErosion(frame)
        cv.imshow("Dilation", dilation)
        cv.imwrite('dilation.png', dilation)
        
        cv.imshow("Erosion", erosion)
        cv.imwrite('erosion.png', erosion)
    elif cv.waitKey(1) == ord('q'):
        break

    
video.release()
cv.destroyAllWindows()