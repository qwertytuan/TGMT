import cv2
from sympy.polys.polyoptions import Gaussian
from Anh import Anh,AnhNew

img = cv2.imread(Anh)
cv2.namedWindow("Goc")
cv2.resize(img, None, fx = 5, fy = 5)

Gaussian = 1

def get_Gauss(pos):
    global Gaussian
    Gaussian = pos
    if Gaussian % 2 == 0:
        Gaussian += 1
        

cv2.createTrackbar("Kernel", "Goc", Gaussian, 50, get_Gauss)
while True:
   
    img_gauss = cv2.GaussianBlur(img, (Gaussian, Gaussian), 9)
    cv2.imshow("Goc", img_gauss)
    #Save anh
    if cv2.waitKey(20) == ord("s"):
        cv2.imwrite(AnhNew, img_gauss)
        
    if cv2.waitKey(20) == ord("q"):
        break

cv2.destroyAllWindows()