import cv2
import matplotlib.pyplot as plt
from Anh import Anh

img = cv2.imread(Anh)
img2 = cv2.resize(img, None, fx = 1.5, fy = 1.5)
cv2.imshow(f'Anh moi = {img.shape[:2]} x1.5', img2)
print(img2.shape[:2])
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.resize