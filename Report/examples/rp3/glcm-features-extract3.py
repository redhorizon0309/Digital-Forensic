import cv2 as cv
import numpy as np
import math as m

img=cv.imread('test3.jpg', cv.IMREAD_GRAYSCALE) 


#Creating Grayscale level co-occurrence matrix
col = img.shape[0]
row = img.shape[1]
intglcm = np.zeros((256, 256),dtype=np.uint32)
glcm = np.zeros((256, 256),dtype=np.float32)
for i in range(0,col-1,1):
    for j in range(0,row-2,1):
        intglcm[img[i][j]][img[i][j+1]]+=1

intglcm = np.transpose(intglcm)+intglcm;
sum = 0
for i in range(0,255):
    for j in range(0,255):
        sum += intglcm[i][j]

for i in range(0,256):
    for j in range(0,256):
        glcm[i][j] = intglcm[i][j]/sum


#Some features extracted from the GLCM
energy = 0
homogeneity = 0
contrast = 0
entropy = 0
for i in range(0, 256):
    for j in range(0, 256):
        energy += np.float(glcm[i][j]*glcm[i][j])
        homogeneity += np.float(glcm[i][j]/(1+abs(i-j)))
        contrast += float((i-j)*(i-j))*glcm[i][j]
        if (glcm[i][j] != 0):
            entropy -= float(glcm[i][j]*m.log(glcm[i][j],10))


print("energy: "+str(energy))
print("homogeneity: "+str(homogeneity))
print("contrast: "+str(contrast))
print("entropy: "+str(entropy))


