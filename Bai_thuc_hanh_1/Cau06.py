import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread("/home/tuan/Downloads/Telegram Desktop/CV/Bai_thuc_hanh_1/Example.jpg")
# gray_img = cv.imread('/home/tuan/Downloads/Telegram Desktop/CV/Bai_thuc_hanh_1/Example_gray_img.jpg')
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title('Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(gray_img, cmap='gray')
plt.title('Gray Image')
plt.axis('off')
plt.show()