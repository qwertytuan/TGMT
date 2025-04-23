import cv2
import numpy as np
from Anh import Anh

# Read the image
img = cv2.imread(Anh)
width,height= 250,350
# Define the points
pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
pts2= np.float32([[0,0],[width,0],[0,height],[width,height]])
# print(pts1)
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
# Draw circles at the defined points
# cv2.circle(img, (int(pts1[0][0]), int(pts1[0][1])), 5, (0, 0, 255), cv2.FILLED)
# cv2.circle(img, (int(pts1[1][0]), int(pts1[1][1])), 5, (0, 0, 255), cv2.FILLED)
# cv2.circle(img, (int(pts1[2][0]), int(pts1[2][1])), 5, (0, 0, 255), cv2.FILLED)
# cv2.circle(img, (int(pts1[3][0]), int(pts1[3][1])), 5, (0, 0, 255), cv2.FILLED)
for x in range(0,4):
    cv2.circle(img, (int(pts1[x][0]), int(pts1[x][1])), 100, (0, 0, 255),)
    cv2.line(img, (int(pts1[x][0]), int(pts1[x][1])), (int(pts1[(x+1)%4][0]), int(pts1[(x+1)%4][1])), (0, 0, 255), 2)
    cv2.rectangle(img, (int(pts1[x][0]), int(pts1[x][1])), (int(pts1[(x+1)%4][0]), int(pts1[(x+1)%4][1])), (0, 0, 255), 2)
    cv2.putText(img, f'({int(pts1[x][0])},{int(pts1[x][1])})', (int(pts1[x][0]), int(pts1[x][1] - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    
cv2.imshow("original img", img)
cv2.imshow("imgOutput",imgOutput )
cv2.waitKey(0)
cv2.destroyAllWindows()


