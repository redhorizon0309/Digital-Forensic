import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
imgForme = cv.imread('forme1.png',0)
imgHouse = cv.imread('house8.png',0)
imgWoman = cv.imread('femme.png',0)
ret,formeimgbin = cv.threshold(imgForme,127,255,cv.THRESH_BINARY)
ret,formeimgbininv = cv.threshold(imgForme,127,255,cv.THRESH_BINARY_INV)
ret,houseimgbin = cv.threshold(imgHouse,127,255,cv.THRESH_BINARY)
ret,houseimgbininv = cv.threshold(imgHouse,127,255,cv.THRESH_BINARY_INV)
ret,womanimgbin = cv.threshold(imgWoman,127,255,cv.THRESH_BINARY)
ret,womanimgbininv = cv.threshold(imgWoman,127,255,cv.THRESH_BINARY_INV)
titles = ['Forme1','Forme1_BINARY','Forme1_BINARY_INV','House8','House8_BINARY','House8_BINARY_INV', 'Woman','Woman_BINARY','Woman_BINARY_INV']
images = [imgForme, formeimgbin, formeimgbininv, imgHouse, houseimgbin, houseimgbininv, imgWoman, womanimgbin, womanimgbininv]
for i in range(9):
    plt.subplot(3,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()