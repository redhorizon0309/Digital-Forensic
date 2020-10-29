from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np

src = cv.imread('cadastre2.png',cv.IMREAD_GRAYSCALE)
objImg = np.ones((1315, 1915),np.uint8)
objImg = src[35:1350,35:1950]
cv.rectangle(objImg,(1650,0),(1915,140),(255,255,255),-1)

ret,obj = cv.threshold(objImg,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

ret,thickObj = cv.threshold(objImg,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
kernel = np.ones((3,3),np.uint8)
thickObj = cv.dilate(thickObj,kernel,iterations = 1)

thinObj = obj - thickObj
ret,thinObj = cv.threshold(thinObj,0,255,cv.THRESH_BINARY_INV)


titles = ['Original','Object','Thick object','Thin object']
images = [src,obj,thickObj,thinObj]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
