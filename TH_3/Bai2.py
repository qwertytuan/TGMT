import cv2 as cv

cap = cv.VideoCapture('TH_3/bai2.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    
    if cv.waitKey(23) ==ord('x'):
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        gray = cv.GaussianBlur(gray, (5, 5), 0)
        laplace= cv.Laplacian(gray, cv.CV_64F, ksize=3)
        laplace = cv.convertScaleAbs(laplace)
        cv.imwrite('TH_3/laplace.jpg', laplace)
        
    cv.imshow('Original', frame)
    if cv.waitKey(23) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()


    
