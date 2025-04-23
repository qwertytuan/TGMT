import cv2
import matplotlib.pyplot as plt
from Anh import Anh

img = cv2.imread(Anh)
h,w = img.shape[:2]
crop = img[:, :w//2]
gray_crop = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
negative_crop = 255 - crop


plt.figure(figsize=(10, 5))

plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Anh goc')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB))
plt.title('Cat anh')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(gray_crop, cmap='gray')
plt.title('Anh xam')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(cv2.cvtColor(negative_crop, cv2.COLOR_BGR2RGB))
plt.title('Anh nghich dao')
plt.axis('off')

plt.show()