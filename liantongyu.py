# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 16:24:57 2019

@author: xiepeng
"""
import cv2
import numpy as np
im=cv2.imread('C:\\Users\\LKJ\\Desktop\\liantogyu.bmp')
w,h,n= im.shape
im_gray = cv2.cvtColor(im,cv2.COLOR_RGB2GRAY)
_,thresh = cv2.threshold(im_gray,128,255,cv2.THRESH_BINARY)
cv2.imshow('th',thresh)
nccomps = cv2.connectedComponentsWithStats(thresh)#labels,stats,centroids
_ = nccomps[0]
labels = nccomps[1]
centroids = nccomps[3]
status = nccomps[2]
for row in range(status.shape[0]):
    if status[row,:][0] == 0 and status[row,:][1] == 0:
        background = row
    else:
       continue
status_no_background = np.delete(status,background,axis=0)
rec_value_max = np.asarray(status_no_background[:,4].max())
re_value_max_position = np.asarray(status_no_background[:,4].argmax())
h = np.asarray(labels,'uint8') 
h[h==(re_value_max_position+1)]=255
for single in range(centroids.shape[0]):
    print(tuple(map(int,centroids[single])))
    #position = tuple(map(int,centroids[single]))
    #cv2.circle(h, position, 1, (255,255,255), thickness=0,lineType=8)
cv2.imshow('h',h)
cv2.imshow('im_bw',thresh)
cv2.imshow('im_origin',im)
cv2.waitKey(0)
cv2.destroyAllWindows()


