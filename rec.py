# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:37:31 2019

@author: LKJ
"""
import cv2
import numpy as np
import random
def draw_dash_rect(img,x1,y1,x2,y2,color):
    clip_slice = 5
    x1_up = x1
    x1_down = x1
    y1_left = y1
    y1_right = y1
    line_dash_up =[]
    line_dash_down =[]
    line_dash_left =[]
    line_dash_right =[]
    number_x_clip = int((x2-x1)/clip_slice)
    number_y_clip = int((y2-y1)/clip_slice)
    for i_x in range(number_x_clip):
        line_dash_up.append((x1_up,y1))
        x1_up+=clip_slice
    for i_xx in range(number_x_clip):
        line_dash_down.append((x1_down,y2))
        x1_down+=clip_slice
    for i_xxx in range(number_y_clip):
        line_dash_left.append((x1,y1_left))
        y1_left+=clip_slice
    for i_xxx in range(number_y_clip):
        line_dash_right.append((x2,y1_right))
        y1_right+=clip_slice
    for point_up in line_dash_up:
        cv2.circle(img, point_up, 1, color, thickness=0,lineType=8)
    for point_down in line_dash_down:
        cv2.circle(img, point_down, 1, color, thickness=0,lineType=8)
    for point_left in line_dash_left:
        cv2.circle(img, point_left, 1, color, thickness=0,lineType=8)
    for point_right in line_dash_right:
        cv2.circle(img, point_right, 1, color, thickness=0,lineType=8)
    cv2.circle(img,(x2,y2),1,color,thickness=0,lineType=8)
    return img

    
canvas = np.zeros((500, 500, 3), dtype="uint8")
canvass = np.zeros((500, 500, 3), dtype="uint8")
pointss = np.zeros((600,600,3),dtype="uint8")
point_size = 1
point_color = (0,0,255)
#points_list = [(160, 160), (165, 160), (170, 160), (175, 160), (180, 160), (185, 160)]
#caption = 'text'
green = (0,255,0)
red = (0,0,255)
yellow = (65,254,254)
x1=100
y1=100
x2=200
y2=200
x1_line=int((x2+x1)/2+random.randint(-15,15))
y1_line=int(y1-85+random.randint(-10,10))
x2_line=int((x2+x1)/2)
y2_line=int(y1)
im_s = draw_dash_rect(canvas,x1,y1,x2,y2,red)

#b = np.array((x1_line,y1_line,x2_line,y2_line)).astype(int)
#for point in points_list:
#	cv2.circle(pointss, point, point_size, point_color, thickness=0,lineType=8)
#cv2.putText(canvas, caption, (x1_line, y1_line), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
#cv2.line(canvas,(x1_line, y1_line), (x2_line, y2_line),yellow,1)
#cv2.rectangle(canvas, (x2, y2), (x1, y1), green,0)
#cv2.rectangle(canvas,(x1,y1),(x2,y2),red,0)
cv2.rectangle(canvass,(x1,y1),(x2,y2),red,0)
cv2.imshow("Canvas", canvas) 
cv2.imshow("canvass",canvass)
#cv2.imshow("pointss",pointss)
#cv2.imshow("dash_rect",im_s)
cv2.waitKey(0) 
cv2.destroyAllWindows()
