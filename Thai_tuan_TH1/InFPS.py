import cv2

video = cv2.VideoCapture('/home/tuan/Downloads/Telegram Desktop/CV/Bai_thuc_hanh_1/Video.mp4')
if not video.isOpened():
    print('Video khong ton tai!!')
else:
    fps = video.get(cv2.CAP_PROP_FPS)
    print(f'So hinh tren giay {fps}')
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f'So khung hinh: {frame_count}')

while True:
        ret, frame = video.read()
        if ret:
            gray_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Video', gray_video)
        if cv2.waitKey(25) == ord('q'):break

video.release()
cv2.destroyAllWindows()