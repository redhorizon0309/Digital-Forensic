from __future__ import print_function
from __future__ import division
import cv2 as cv
import numpy as np
import argparse
parser = argparse.ArgumentParser(description='Code for Histogram Calculation tutorial.')
parser.add_argument('--input', help='Path to input image.', default='aquitaine.png')
args = parser.parse_args()
src = cv.imread(cv.samples.findFile(args.input))
if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)

#add 100 intensity to each pixel
blank=np.zeros([256,256,3],dtype=np.uint8)
blank.fill(100)
img100=cv.add(src,blank)

bgr_planes = cv.split(src)
bgr_planes100 = cv.split(img100)
histSize = 256
histRange = (0, 256) # the upper boundary is exclusive
accumulate = False
b_hist = cv.calcHist(bgr_planes, [0], None, [histSize], histRange, accumulate=accumulate)
g_hist = cv.calcHist(bgr_planes, [1], None, [histSize], histRange, accumulate=accumulate)
r_hist = cv.calcHist(bgr_planes, [2], None, [histSize], histRange, accumulate=accumulate)
b_hist100 = cv.calcHist(bgr_planes100, [0], None, [histSize], histRange, accumulate=accumulate)
g_hist100 = cv.calcHist(bgr_planes100, [1], None, [histSize], histRange, accumulate=accumulate)
r_hist100 = cv.calcHist(bgr_planes100, [2], None, [histSize], histRange, accumulate=accumulate)
hist_w = 512
hist_h = 400
bin_w = int(round( hist_w/histSize ))
histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
histImage100 = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
cv.normalize(b_hist, b_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(g_hist, g_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(r_hist, r_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(b_hist100, b_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(g_hist100, g_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(r_hist100, r_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
for i in range(1, histSize):
    cv.line(histImage, ( bin_w*(i-1), hist_h - int(np.round(b_hist[i-1])) ),( bin_w*(i), hist_h - int(np.round(b_hist[i])) ),( 255, 0, 0), thickness=2)
    cv.line(histImage, ( bin_w*(i-1), hist_h - int(np.round(g_hist[i-1])) ),( bin_w*(i), hist_h - int(np.round(g_hist[i])) ),( 0, 255, 0), thickness=2)
    cv.line(histImage, ( bin_w*(i-1), hist_h - int(np.round(r_hist[i-1])) ),( bin_w*(i), hist_h - int(np.round(r_hist[i])) ),( 0, 0, 255), thickness=2)
    cv.line(histImage100, ( bin_w*(i-1), hist_h - int(np.round(b_hist100[i-1])) ),( bin_w*(i), hist_h - int(np.round(b_hist100[i])) ),( 255, 0, 0), thickness=2)
    cv.line(histImage100, ( bin_w*(i-1), hist_h - int(np.round(g_hist100[i-1])) ),( bin_w*(i), hist_h - int(np.round(g_hist100[i])) ),( 0, 255, 0), thickness=2)
    cv.line(histImage100, ( bin_w*(i-1), hist_h - int(np.round(r_hist100[i-1])) ),( bin_w*(i), hist_h - int(np.round(r_hist100[i])) ),( 0, 0, 255), thickness=2)

cv.imshow('aquitaine.png', src)
cv.imshow('aquitainehist', histImage)

cv.imshow('aquitaine+100', img100)
cv.imshow('aquitaine+100hist', histImage100)
cv.waitKey()