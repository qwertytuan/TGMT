import cv2
import numpy as np
from Anh import Anh

img=cv2.imread(Anh)
cv2.circle(img, (111, 219),100 , (255, 255, 255))
cv2.line(img, (500, 600), (287, 188), (255, 255, 255), 1)
cv2.rectangle(img, (500, 500), (700, 700), (255, 255, 255), 1)
cv2.rectangle(img, (500, 219), (787, 288), (255, 255, 255), 1)
cv2.putText(img, f'(111,219)', (111, 219 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
cv2.ellipse(img, (154, 482), (100, 50), 90, 0, 360, (255, 255, 255), 1)
cv2.imshow("original img", img)
while True:
    if cv2.waitKey(20)== ord('q'):
        break
cv2.destroyAllWindows()