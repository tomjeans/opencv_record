# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:05:37 2019

@author: xiepeng
"""
import cv2
import numpy as np
img = cv2.imread('C:\\Users\\LKJ\\Desktop\\predictions.png',0)
#cv2.imshow('im',im)
img[img==127]=0
#_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
image, contours, hierarchy = cv2.findContours(img, 3, 2)
cnt = contours[0]
img_color1 = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
img_color2 = np.copy(img_color1)
img_color3 = np.zeros((img.shape[0],img.shape[1],3),dtype="uint8")
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
print(box)
cv2.drawContours(img_color1, [box], 0, (255, 0, 0), 2)
#im[im==255]=1
point_line_1=(int((box[0][0]+box[3][0])/2),int((box[0][1]+box[3][1])/2))
point_line_2=(int((box[1][0]+box[2][0])/2),int((box[1][1]+box[2][1])/2))
print(point_line_1)
print(point_line_2)
img_color2[img_color2==255]=60
cv2.line(img_color3,point_line_1,point_line_2,(0,127,0),1)
cv2.line(img_color1,point_line_1,point_line_2,(0,127,0),1)
green=img_color2[:,:,1]
green_im_color=img_color3[:,:,1]

#cv2.imshow('line_in_source',green)
#cv2.imshow('line_bg',img_color3[:,:,1])
img_end=img_color3[:,:,1]+img_color2[:,:,1]
#cv2.imshow('img_end',img_end)
length=np.sum(img_end==187)
cv2.putText(img_color1, 'fl_length:'+str(length), (30, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 1)
cv2.imshow('im',img_color1)
print('fl_length:',length)
cv2.waitKey(0)
cv2.destroyAllWindows()

#key = np.unique(y)
#result = {}
#for k in key:
#    mask = (y == k)
#    y_new = y[mask]
#    v = y_new.size
#    result[k] = v
#print(result)
#cv2.imshow('im_bw',cnt)
#cv2.imshow('im_rec_out',im)


