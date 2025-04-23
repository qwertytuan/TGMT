import cv2


video = cv2.VideoCapture()
if not video.isOpened():
    print('Video khong ton tai!!')
else:
    fps = video.get(cv2.CAP_PROP_FPS)
    print(f'So hinh tren giay {fps}')
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f'So khung hinh: {frame_count}')


while True:
    ret, frame = video.read()
    if not ret:
        break
    cv2.imshow("Video", frame)
    
    if cv2.waitKey(20) == ord("s"):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(VideoSave, gray_frame)
        print("Saved")
    elif cv2.waitKey(20) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()