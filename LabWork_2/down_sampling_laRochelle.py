import sys
import cv2 as cv

img = cv.imread("LaRochelle.jpg")
if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Original", img)
print(img.shape)

dim300=(int(img.shape[1]*30/43),int(img.shape[0]*30/43))
dim25=(int(img.shape[1]*5/86),int(img.shape[0]*5/86))
img300=cv.resize(img,dim300, interpolation=cv.INTER_AREA)
img25=cv.resize(img,dim25, interpolation=cv.INTER_AREA)
#cv.imshow("LaRochelle50.png", img300)
#cv.imshow("LaRochelle25.png", img25)
cv.imwrite("LaRochelle300.png", img300)
cv.imwrite("LaRochelle25.png", img25)
cv.waitKey(0)