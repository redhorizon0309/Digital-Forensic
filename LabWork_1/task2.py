import cv2 as cv
import numpy as np
import sys

img = cv.imread("logo-usth.png")
imgb = np.zeros((1125,2000,3), np.uint8)

if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Original", img)
print(img.shape)

b,g,r=cv.split(img)
#cv.imshow("Blue Channel",b)
#cv.imshow("Green Channel",g)
#cv.imshow("Red Channel",r)

red  = np.full((1125,2000,3), (0,0,255), np.uint8)
blue  = np.full((1125,2000,3), (255,0,0), np.uint8)
imgRed  = cv.addWeighted(img, 0.8, red, 0.2, 0)
imgBlue  = cv.addWeighted(img, 0.8, blue, 0.2, 0)

cv.imshow("Blue", imgBlue)
cv.imshow("Red", imgRed)
#cv.imshow("Green", imgGreen)

cv.waitKey(0)