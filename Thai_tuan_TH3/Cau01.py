import cv2
import matplotlib.pyplot as plt
from Anh import Anh

img = cv2.imread(Anh)
img = cv2.resize(img, None, fx = 2, fy = 2)



img_blur = cv2.blur(img, (5,5))

img_median = cv2.medianBlur(img, 5)

img_gauss = cv2.GaussianBlur(img, (5,5), 9)

img_bilateral = cv2.bilateralFilter(img, 9, 50, 50)

#Chuyển sang RGB

blur = cv2.cvtColor(img_blur, cv2.COLOR_BGR2RGB)
median = cv2.cvtColor(img_median, cv2.COLOR_BGR2RGB)
gauss = cv2.cvtColor(img_gauss, cv2.COLOR_BGR2RGB)
bilateral = cv2.cvtColor(img_bilateral, cv2.COLOR_BGR2RGB)

# new_blur = img_blur
# new_median = img_median
# new_gauss = img_gauss
# new_bilateral = img_bilateral

plt.subplot(221)
plt.title("Blur")
plt.axis("off")
plt.imshow(blur)

plt.subplot(222)
plt.title("Median")
plt.axis("off")
plt.imshow(median)

plt.subplot(223)
plt.title("Gauss")
plt.axis("off")
plt.imshow(gauss)

plt.subplot(224)
plt.title("Bilateral")
plt.axis("off")
plt.imshow(bilateral)

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()