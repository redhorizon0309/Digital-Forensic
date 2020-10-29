from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np


imgForme = cv.imread('forme3.png',0)
histSize = 256
histRange = (0, 256)
histForme=cv.calcHist(imgForme, [0], None, [histSize], histRange, accumulate=False)
ret,imgFormeBin=cv.threshold(imgForme,105,130,cv.THRESH_BINARY)
histFormeBin=cv.calcHist(imgFormeBin, [0], None, [histSize], histRange, accumulate=False)

hist_w = 256
hist_h = 300
bin_w = int(round( hist_w/histSize ))

histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
histImageBin = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)

cv.normalize(histForme, histForme, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(histFormeBin, histFormeBin, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)

for i in range(1, histSize):
    cv.line(histImage, ( bin_w*(i-1), hist_h - int(np.round(histForme[i-1])) ),( bin_w*(i), hist_h - int(np.round(histForme[i])) ),( 255, 255, 255), thickness=2)
    cv.line(histImageBin, ( bin_w*(i-1), hist_h - int(np.round(histFormeBin[i-1])) ),( bin_w*(i), hist_h - int(np.round(histFormeBin[i])) ),( 255, 255, 255), thickness=2)

titles = ['Forme1','hist','imgFormeBin','histImageBin']
images = [imgForme,histImage,imgFormeBin,histImageBin]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()