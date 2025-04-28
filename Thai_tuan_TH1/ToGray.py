import cv2

img = cv2.imread("/home/tuan/Downloads/Telegram Desktop/CV/Bai_thuc_hanh_1/Example.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray_img)
cv2.imwrite('./Example_gray_img.jpg', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
