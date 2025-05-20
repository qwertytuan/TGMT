import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread('TH_3/bai1.jpg')
h_old,w_old= image.shape[:2]

w = int(input(f'nhap chieu rong(<={w_old}): '))
h = int(input(f'nhap chieu cao(<={h_old}): '))
if w < 0 or h < 0:
    print('chieu rong va chieu cao phai > 0')
    exit()
if w > w_old or h > h_old:
    print('chieu rong va chieu cao phai < chieu rong va chieu cao ban dau')
    exit()
    
image_resize = cv.resize(image, (w, h), interpolation=cv.INTER_CUBIC)
image_gray = cv.cvtColor(image_resize, cv.COLOR_BGR2GRAY)
image_gray = cv.GaussianBlur(image_gray, (5, 5), 0)
iamage_adpt = cv.adaptiveThreshold(image_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

plt.figure(figsize=(10, 10))

image_rgb=cv.cvtColor(image, cv.COLOR_BGR2RGB)
plt.subplot(221)
plt.title('image')
plt.imshow(image_rgb)

plt.subplot(222)
plt.imshow(cv.cvtColor(image_resize,cv.COLOR_BGR2RGB))
plt.title('image resize')


plt.subplot(223)
plt.imshow(iamage_adpt, 'gray')
plt.title('image adaptive')


plt.savefig('TH_3/image.png')
