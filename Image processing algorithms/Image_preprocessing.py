# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 20:00:51 2020

@author: LENOVO
"""

import cv2
import numpy as np


############################################################################# 


#img = cv2.imread("est.jpg")
#
#
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#edges = cv2.Canny(gray, 75, 150)
#
#lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50)
#
#lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=250)

############################################################################# working fine

image = cv2.imread("test-600.png")
image = cv2.resize(image,(128,128))
cv2.imshow('Orginal Image', image)
print(image)
cv2.waitKey()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #step 1--------------->convert image to grayscale
cv2.imshow('gray Image', gray)
cv2.waitKey()
sharpen_kernel = np.array([[-1,-1,-1], [-1,10,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
cv2.imshow('thresh', thresh)
cv2.waitKey()

#dose not work
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
cv2.imshow('close', close)
cv2.waitKey()
result = 255 - close
cv2.imshow('result', result)
#cv2.waitKey()


#Image Erosion
kernel = np.ones((2,2),np.uint8)
erosion = cv2.erode(result,kernel,iterations = 1)
cv2.imshow('erosion', erosion)
cv2.waitKey()

#Image Dilation
#dilation = cv2.dilate(result,kernel,iterations = 1)
#cv2.imshow('dilation', dilation)
#cv2.waitKey()

#Image opening
opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
cv2.imshow('opening', opening)
cv2.waitKey()


#Image closing
closing = cv2.morphologyEx(erosion, cv2.MORPH_CLOSE, kernel)
cv2.imshow('closing', closing)
cv2.waitKey()


#cv2.imshow('sharpen', sharpen)
#cv2.imshow('thresh', thresh)
#cv2.imshow('close', close)
#cv2.imshow('result', result)
#cv2.waitKey()


############################################################################# dose not work

#
#img = cv2.imread("est.jpg", 0)
#ret, thresh = cv2.threshold(img, 10, 255, cv2.THRESH_OTSU)
#
#print ("Threshold selected : ", ret)
#cv2.imwrite("./debug.jpg", thresh)


#############################################################################




mm

