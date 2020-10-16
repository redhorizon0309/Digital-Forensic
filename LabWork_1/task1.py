import cv2 as cv
import sys

img = cv.imread("football.jpeg")

if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Original", img)

imgPurple=img[70:240,90:200]
imgRed=img[80:240,250:340]
imgBall=img[190:220,205:240]
cv.imshow("Purple", imgPurple)
cv.imshow("Red", imgRed)
cv.imshow("Ball", imgBall)

cv.waitKey(0)