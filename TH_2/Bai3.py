import cv2 as cv

cap = cv.VideoCapture('Thai_tuan_TH4/Video.mp4')
isGray = False

def toggle_gray():
    global isGray
    isGray = not isGray

while cap:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv.resize(frame, (1366, 768))
    
    if isGray:
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)


    cv.imshow('Video', frame)
    
    if cv.waitKey(10) == ord('g'):
        toggle_gray() 
    elif cv.waitKey(10) == ord('s'):
        cv.imwrite('Thai_tuan_TH4/VideoSave.png', frame)
        print("Saved")
    elif cv.waitKey(10) == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()
