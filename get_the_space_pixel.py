# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:14:04 2019

@author: Xiepeng
"""
import cv2
import numpy as np
def get_the_pixel_space(path):
    i = 0
    scale=53/1130
    l = []
    im_test_original = cv2.imread(path)
    height,width,dim=im_test_original.shape
    im_black_mask = np.zeros((height,width),dtype=np.uint8)
    im_black_mask[0:height,0:int(width*scale)]=255
    hsv = cv2.cvtColor(im_test_original,cv2.COLOR_BGR2HSV)
    print(im_test_original.shape)
    #cv2.imshow('black',im_black_mask)
    #cv2.imshow('hsv_original',hsv)
    
    low_hsv = np.array([26,43,46],dtype = np.uint8)
    upper_hsv = np.array([34,255,255],dtype = np.uint8)
    mask_ = cv2.inRange(hsv,low_hsv,upper_hsv)
    #image_res=cv2.add(mask_, np.zeros(np.shape(mask_), dtype=np.uint8), mask=im_black_mask)
    res=cv2.bitwise_and(mask_,im_black_mask)
    #edges = cv2.Canny(res, 50, 150, apertureSize=3)
    res[res!=0]=1
    minLineLength = 3
    maxLineGap = 0.5
    lines = cv2.HoughLinesP(res, 1, np.pi / 180, 1, minLineLength, maxLineGap)
    
    for x1, y1, x2, y2 in lines[:,0,:]:
        print('x1_y1_x2_y2:',x1,y1,x2,y2)
        l.append(y1)
        i+=1
        #cv2.line(im_test_original, (x1, y1), (x2, y2), (0, 255, 0), 2)
    #cv2.imshow('edges',edges)
    print('mask_',mask_.shape)
    print('im_black_nask',im_black_mask.shape)
    print('counts_of_line',i)
    print('l',l)
    m=set(l)
    m=list(m)
    m.sort()
    print('l',m)
    values = [m[ii+1]-m[ii] for ii in range(len(m)-1)]
    print('values:',values)
    space_pixel_cm=max(values, key=values.count)
    print('space_pixel_cm:',space_pixel_cm)
    pixel_space = 1/space_pixel_cm
    print('pixel_space:',pixel_space)
    #cv2.imshow("result",mask_)
    #cv2.imshow("result_r",im_test_original)
    #scale=53/1130
    #space_pixel_region = ((0,0),(image.shape[1]*scale,image.shape[0]))
    #cv2.waitKey(0)
    return pixel_space


