from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np

src = cv.imread('cadastre1.png',0)

textMask = cv.imread('cadastre1.png',0)
cv.rectangle(textMask,(290,140),(800,560),(0,0,0),-1)
cv.rectangle(textMask,(150,360),(290,480),(0,0,0),-1)
cv.rectangle(textMask,(800,360),(900,480),(0,0,0),-1) 
textImg= src - textMask

whiteBg = np.full(textMask.shape,255,dtype=np.uint8)
cv.rectangle(textMask,(290,140),(800,560),(0,0,0),-1)
cv.rectangle(textMask,(150,360),(290,480),(0,0,0),-1)
cv.rectangle(textMask,(800,360),(900,480),(0,0,0),-1) 
textImg = textImg + whiteBg

kernel = np.ones((3,3),np.uint8)
textErode = cv.erode(textImg,kernel,iterations = 1)

textMorph = cv.morphologyEx(textErode, cv.MORPH_CROSS, kernel)

textBlur = cv.GaussianBlur(textMorph,(1,1),0)
ret,clearText = cv.threshold(textBlur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

titles = ['Original','Clear text']
images = [src,clearText]
for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
