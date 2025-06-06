import cv2 as cv

cap = cv.VideoCapture('TH_3/bai2.mp4')
fps = cap.get(cv.CAP_PROP_FPS)
cap.set(cv.CAP_PROP_HW_ACCELERATION,2)
length = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
time= int(length/fps)
print(time)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    
    if cv.waitKey(time) ==ord('x'):
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        gray = cv.GaussianBlur(gray, (5, 5), 0)
        laplace= cv.Laplacian(gray, cv.CV_64F, ksize=3)
        laplace = cv.convertScaleAbs(laplace)
        cv.imwrite('TH_3/laplace.jpg', laplace)
        
    cv.imshow('Original', frame)
    if cv.waitKey(time) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()


    
