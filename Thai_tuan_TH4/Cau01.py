
import cv2 as cv
import matplotlib.pyplot as plt
from AnhTh4 import Anh

image = cv.imread(Anh)

image_rgb= cv.cvtColor(image, cv.COLOR_BGR2RGB)

image_gauss= cv.GaussianBlur(image, (5, 5), 0)

image_gray = cv.cvtColor(image_gauss, cv.COLOR_BGR2GRAY)

ret, image_otsu= cv.threshold(image_gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

plt.subplot(1,3,1)
plt.title('Goc')
plt.axis('off')
plt.imshow(image_rgb)

plt.subplot(1,3,2)
plt.title('Gray')
plt.axis('off')
plt.imshow(image_gray, cmap='gray')

plt.subplot(1,3,3)
plt.title('Otsu')
plt.axis('off')
plt.imshow(image_otsu, cmap='gray')

plt.savefig('/Thai_tuan_TH4/Cau01.png')

cv.waitKey(0)
cv.destroyAllWindows()



