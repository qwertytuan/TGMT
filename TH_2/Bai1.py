import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('/mnt/01DB783D25219E60/HOMEWORK/TGMT/TH_1/pic.png')
img = img[0:640, 0:640]
cv.imshow("Goc", img)
cv.waitKey(0)
cv.destroyAllWindows()


h,w= img.shape[:2]
print(f"Height: {h}, Width: {w}")

x1 = int(input("Nhap toa do x1 :"))
y1 = int(input("Nhap toa do y1 :"))
x2 = int(input("Nhap toa do x2 :"))
y2 = int(input("Nhap toa do y2 :"))


if x1 < 0 or y1 < 0 or x2 > w or y2 > h or x1 >= x2 or y1 >= y2:
    print("Loi.")
    exit()


cropped_img = img[y1:y2, x1:x2]


gray_img = cv.cvtColor(cropped_img, cv.COLOR_BGR2GRAY)


_, thresh_img = cv.threshold(gray_img, 100, 255,cv.THRESH_OTSU)


plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title("Goc")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(cv.cvtColor(cropped_img, cv.COLOR_BGR2RGB))
plt.title("Cat")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(thresh_img, cmap="gray")
plt.title("Otsu")
plt.axis("off")
plt.tight_layout()

plt.savefig("TH_2/Bai1.png")
