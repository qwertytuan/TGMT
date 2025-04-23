import cv2

video = cv2.VideoCapture("/home/tuan/Downloads/Telegram Desktop/CV/Bai_thuc_hanh_1/Video.mp4")
if not video.isOpened():
    print("Video khong ton tai!!!")
while True:
    ret,frame = video.read()
    if ret:
        cv2.imshow('Video', frame)

    if cv2.waitKey(25) == ord('s'):
       cv2.imwrite("./Video_Screenshot.jpg", frame)
       print('Da chup anh')
    if cv2.waitKey(25) == ord('q'):
        cv2.destroyAllWindows()
        break
    
video.release()
cv2.destroyAllWindows()