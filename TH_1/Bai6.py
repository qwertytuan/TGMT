import cv2 as cv


video = cv.VideoCapture('./Thai_tuan_TH4/Video.mp4')

if not video.isOpened():
    print('Video khong ton tai!!')
else:
    fps = video.get(cv.CAP_PROP_FPS)
    frame_count = int(video.get(cv.CAP_PROP_FRAME_COUNT))
    print(f'So khung hinh: {frame_count}')


while True:
    ret, frame = video.read()
    frame = cv.resize(frame, (640, 640))
    
    cv.putText(frame, f'So hinh tren giay {fps}', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    if not ret:
        break
    cv.imshow("Video", frame)
    cv.imshow("Video_gray", cv.cvtColor(frame, cv.COLOR_BGR2GRAY))
    if cv.waitKey(1) == ord('q'):
        break
    

video.release()
cv.destroyAllWindows()