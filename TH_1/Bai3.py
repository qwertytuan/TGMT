import cv2 as cv
import matplotlib.pyplot as plt

image_goc = cv.imread('pic.png')

w = int(input("Enter width: "))
h = int(input("Enter height: "))
image_resize = cv.resize(image_goc, (w, h))

image_gray = cv.cvtColor(image_resize, cv.COLOR_BGR2GRAY)
image_blur = cv.GaussianBlur(image_gray, (5, 5), 0)


sobelX = cv.Sobel(image_blur, cv.CV_64F, 1, 0, ksize=5)
sobelY = cv.Sobel(image_blur, cv.CV_64F, 0, 1, ksize=5)
sobel = cv.addWeighted(sobelX, 0.5, sobelY, 0.5, 0)



plt.subplot(2, 1, 1)
plt.imshow(cv.cvtColor(image_resize, cv.COLOR_BGR2RGB))
plt.title('Anh goc')
plt.axis('off')

plt.subplot(2, 1, 2)
plt.imshow(sobel, cmap='gray')
plt.title('Sobel')
plt.axis('off')


plt.show()
plt.savefig('sobel.png')
    
cv.waitKey(0)
cv.destroyAllWindows()
