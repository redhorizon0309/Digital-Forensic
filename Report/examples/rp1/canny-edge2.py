import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('wallpaper.jpg',0)
edges1 = cv.Canny(img,100,300)
edges2 = cv.Canny(img,50,100)
plt.subplot(121),plt.imshow(edges1,cmap = 'gray')
plt.title('Min:100; Max:300'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges2,cmap = 'gray')
plt.title('Min:50; Max:100'), plt.xticks([]), plt.yticks([])
plt.show()