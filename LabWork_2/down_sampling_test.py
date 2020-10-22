import sys
import cv2 as cv

img = cv.imread("chart_test.png")
if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Original", img)
print(img.shape)
imgsq=img[:,43:1224]
print(imgsq.shape)
dim50=(int(imgsq.shape[1]/2),int(imgsq.shape[0]/2))
dim25=(int(imgsq.shape[1]/4),int(imgsq.shape[0]/4))
img50=cv.resize(imgsq,dim50, interpolation=cv.INTER_AREA)
img25=cv.resize(imgsq,dim25, interpolation=cv.INTER_AREA)
#cv.imshow("chart_test50.png", img50)
#cv.imshow("chart_test25.png", img25)
cv.imwrite("chart_test50.png", img50)
cv.imwrite("chart_test25.png", img25)
cv.waitKey(0)