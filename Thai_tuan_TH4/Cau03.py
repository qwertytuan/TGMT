import cv2 as cv


video = cv.VideoCapture('Thai_tuan_TH4/Video.mp4')

if not video.isOpened():
    print('Video khong ton tai!!')
else:
    fps = video.get(cv.CAP_PROP_FPS)
    print(f'So hinh tren giay {fps}')
    frame_count = int(video.get(cv.CAP_PROP_FRAME_COUNT))
    print(f'So khung hinh: {frame_count}')


while True:
    ret, frame = video.read()
    if not ret:
        break
    cv.imshow("Video", frame)
    
    if cv.waitKey(ord("s")) == ord("s"):
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imwrite('/Thai_tuan_TH4/VideoSave.png', gray_frame)
        print("Saved")
    elif cv.waitKey(20) == ord('q'):
        break

video.release()
cv.destroyAllWindows()