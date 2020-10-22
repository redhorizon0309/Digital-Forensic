from __future__ import print_function
from __future__ import division
import cv2 as cv
import numpy as np
import argparse
parser = argparse.ArgumentParser(description='Code for Histogram Calculation tutorial.')
parser.add_argument('--input', help='Path to input image.', default='tire.png')
args = parser.parse_args()
src = cv.imread(cv.samples.findFile(args.input))
if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)

src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
src = cv.equalizeHist(src)
bgr_planes = cv.split(src)
histSize = 256
histRange = (0, 256) # the upper boundary is exclusive
accumulate = False
hist = cv.calcHist(bgr_planes, [0], None, [histSize], histRange, accumulate=accumulate)
hist_w = 512
hist_h = 400
bin_w = int(round( hist_w/histSize ))
histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
cv.normalize(hist, hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
for i in range(1, histSize):
    cv.line(histImage, ( bin_w*(i-1), hist_h - int(np.round(hist[i-1])) ),( bin_w*(i), hist_h - int(np.round(hist[i])) ),( 255, 0, 0), thickness=2)
cv.imshow('equalized_tire.png', src)
cv.imwrite('equalized_tire.png', src)
cv.imshow('tirehist', histImage)
cv.waitKey()