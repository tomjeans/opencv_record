# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 14:52:42 2019

@author: Xiepeng
"""
list_positons_one= [[22,33],[11,44],[23,10],[33,21],[22,33]]
list_position_second = [[11,33],[15,55],[18,60],[24,77],[30,68],[42,72],[50,61],[10,-20],[20,-30]]
#like (x,y)
#processing the dict_x:y {x_n:y_n} dict_y:x {y_n:x_n}
#first find the medium_number {x_medium:y_n} {y_medium:x_n}
#sort the x from min to max
#dict_x[x_sort] < y_medium distance_y value positivity  
#               > y_medium distance_y value negative
#               = y_medium distance_y value 0 
#x_sort < x_medium distance distance_x value negative 
#       > x_medium distance distance_x value positivity
#       = x_medium distance distance_x value 0
positions=[]
positions_x=[]
positions_y=[]
dict_x={}
dict_y={}
info_distance={}
import cv2
import numpy as np
im=cv2.imread('C:\\Users\\LKJ\\Desktop\\lian_2.jpg')
w,h,n= im.shape
im_gray = cv2.cvtColor(im,cv2.COLOR_RGB2GRAY)
_,thresh = cv2.threshold(im_gray,128,255,cv2.THRESH_BINARY)

nccomps = cv2.connectedComponentsWithStats(thresh)#labels,stats,centroids
centroids = nccomps[3]# center position x,y [[x1,y1],[x2,y2],...[xn,yn]]
cv2.imshow('th',thresh)
for center in centroids:
    ce = (int(center[0]),int(center[1]))
    positions_x.append(int(center[0]))
    positions_y.append(int(center[1]))
    positions.append(ce)
    #cv2.circle(im, ce, 1, (0,0,255), thickness=0,lineType=8)

print(centroids)
#function_start
for positions_single in positions:
    dict_x[positions_single[0]]=positions_single[1]
    dict_y[positions_single[1]]=positions_single[0]
positions_x_sort=sorted(positions_x)
positions_y_sort=sorted(positions_y)
for positions_x_sort_s in positions_x_sort:
    if dict_x[positions_x_sort_s] < positions_y_sort[int(len(positions_y_sort)/2)]:
        distance_y = -88
    elif dict_x[positions_x_sort_s] > positions_y_sort[int(len(positions_y_sort)/2)]:
        distance_y = 88
    else:
        distance_y = 0
    if positions_x_sort_s < positions_x_sort[int(len(positions_x_sort)/2)]:
        distance_x = -20
    elif positions_x_sort_s > positions_x_sort[int(len(positions_x_sort)/2)]:
       distance_x = 20
    else:
       distance_x = 0
    info_distance[(positions_x_sort_s,dict_x[positions_x_sort_s])]=(distance_x,distance_y)
for position_line_start in info_distance:
    cv2.line(im,position_line_start, tuple(np.array(position_line_start)+np.array(info_distance[position_line_start])),(0,0,255),1)
cv2.imshow('im_',im)
cv2.waitKey(0)
cv2.destroyAllWindows()