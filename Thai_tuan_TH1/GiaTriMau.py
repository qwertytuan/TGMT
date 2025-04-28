import cv2 as cv
x = int(input('Nhap toa do x: '))
y = int(input('Nhap toa do y: '))
img = cv.imread("/home/tuan/Downloads/Telegram Desktop/CV/Bai_thuc_hanh_1/Example.jpg")
if 0 <= x < img.shape[1] and 0 <= y < img.shape[1]:
    (b, g, r) = img[y,x]
    color_text=f'Gia tri mau tai ({x}, {y}) la: BRG = ({b}, {g}, {r})'
    cv.putText(img, color_text, (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv.LINE_AA)
    cv.imshow('Hoa hong', img)
else:
    print('Gia tri khong hop le')

cv.waitKey(0)
cv.destroyAllWindows()



