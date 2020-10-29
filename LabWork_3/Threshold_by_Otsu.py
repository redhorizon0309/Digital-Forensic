from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np

imgForme1 = cv.imread('forme1.png',0)
imgForme3 = cv.imread('forme3.png',0)
imgLena = cv.imread('lena.png',0)

ret1,imgFormeBin1=cv.threshold(imgForme1,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
ret2,imgFormeBin3=cv.threshold(imgForme3,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
ret3,imgLenaBin=cv.threshold(imgLena,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

histSize = 256
histRange = (0, 256)
hist_w = 256
hist_h = 300
bin_w = int(round( hist_w/histSize ))

histForme1=cv.calcHist(imgForme1, [0], None, [histSize], histRange, accumulate=False)
histForme3=cv.calcHist(imgForme3, [0], None, [histSize], histRange, accumulate=False)
histLena=cv.calcHist(imgLena, [0], None, [histSize], histRange, accumulate=False)
histBiForme1=cv.calcHist(imgFormeBin1, [0], None, [histSize], histRange, accumulate=False)
histBiForme3=cv.calcHist(imgFormeBin3, [0], None, [histSize], histRange, accumulate=False)
histBiLena=cv.calcHist(imgLenaBin, [0], None, [histSize], histRange, accumulate=False)

histImgForme1 = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
histImgForme3 = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
histImgLena = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
histBiImgForme1 = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
histBiImgForme3 = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
histBiImgLena = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)

cv.normalize(histForme1, histForme1, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(histForme3, histForme3, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(histLena, histLena, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(histBiForme1, histBiForme1, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(histBiForme3, histBiForme3, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(histBiLena, histBiLena, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
for i in range(1, histSize):
    cv.line(histImgForme3, ( bin_w*(i-1), hist_h - int(np.round(histForme1[i-1])) ),( bin_w*(i), hist_h - int(np.round(histForme1[i])) ),( 255, 255, 255), thickness=2)
    cv.line(histImgForme1, ( bin_w*(i-1), hist_h - int(np.round(histForme3[i-1])) ),( bin_w*(i), hist_h - int(np.round(histForme3[i])) ),( 255, 255, 255), thickness=2)
    cv.line(histImgLena, ( bin_w*(i-1), hist_h - int(np.round(histLena[i-1])) ),( bin_w*(i), hist_h - int(np.round(histLena[i])) ),( 255, 255, 255), thickness=2)
    cv.line(histBiImgForme1, ( bin_w*(i-1), hist_h - int(np.round(histBiForme1[i-1])) ),( bin_w*(i), hist_h - int(np.round(histBiForme1[i])) ),( 255, 255, 255), thickness=2)
    cv.line(histBiImgForme3, ( bin_w*(i-1), hist_h - int(np.round(histBiForme3[i-1])) ),( bin_w*(i), hist_h - int(np.round(histBiForme3[i])) ),( 255, 255, 255), thickness=2)
    cv.line(histBiImgLena, ( bin_w*(i-1), hist_h - int(np.round(histBiLena[i-1])) ),( bin_w*(i), hist_h - int(np.round(histBiLena[i])) ),( 255, 255, 255), thickness=2)

titles = ['imgForme1','imgForme3','imgLena','histImgForme1','histImgForme3','histImgLena','imgFormeBin1','imgFormeBin3','imgLenaBin','histBiImgForme1','histBiImgForme3','histBiImgLena']
images = [imgForme1,imgForme3,imgLena,histImgForme1,histImgForme3,histImgLena,imgFormeBin1,imgFormeBin3,imgLenaBin,histBiImgForme1,histBiImgForme3,histBiImgLena]
for i in range(12):
    plt.subplot(4,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()