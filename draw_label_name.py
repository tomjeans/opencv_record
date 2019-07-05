# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 14:52:42 2019

@author: Xiepeng
"""
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
info_label_name={}
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
im=cv2.imread('C:\\Users\\LKJ\\Desktop\\lian_2.jpg')
w,h,n= im.shape
im_gray = cv2.cvtColor(im,cv2.COLOR_RGB2GRAY)
_,thresh = cv2.threshold(im_gray,128,255,cv2.THRESH_BINARY)

nccomps = cv2.connectedComponentsWithStats(thresh)#labels,stats,centroids
centroids = nccomps[3]# center position x,y [[x1,y1],[x2,y2],...[xn,yn]]
#cv2.imshow('th',thresh)
#solve the positions
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
    label_name_start_position = tuple(np.array(position_line_start)+np.array(info_distance[position_line_start]))
    info_label_name[label_name_start_position] = 'test(注意字体使用)'#label_name
    #cv2.putText(im, 'test', label_name_start_position, cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
#info_distance[position_line_start] is (distance_x,distance_y)
#position_line_start is the start point 
im_pil=Image.fromarray(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
font = ImageFont.truetype('Alibaba-PuHuiTi-Regular.otf',22)
for position_label_name in info_label_name:
    label_str = info_label_name[position_label_name]
    # str = str.encode('utf8')
    draw = ImageDraw.Draw(im_pil)
    draw.text(position_label_name, label_str, font=font, fill=(255, 0, 0))
im_show = cv2.cvtColor(np.asarray(im_pil),cv2.COLOR_RGB2BGR)
cv2.imshow('im_',im_show)
cv2.waitKey(0)
cv2.destroyAllWindows()
#########################################################
def draw_labe_name_(positions,positions_x,positions_y,dic_info_label_name):
    import cv2
    import numpy as np
    from PIL import Image, ImageDraw, ImageFont
    '''dic_info_label_name:{(center_x,center_y):label_name_kind}
       positions:[(x1,y1),(x2,y2),..(xn,yn)]
       positions_x:[x1,x3,x2,xn]
       position_y:[y1,y3,y2,yn]
    '''
    positions=[]
    positions_x=[]
    positions_y=[]
    dict_x={}
    dict_y={}
    info_distance={}
    info_label_name={}
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
        label_name_start_position = tuple(np.array(position_line_start)+np.array(info_distance[position_line_start]))
        label_name_pp[position_line_start] = label_name_start_position
        info_label_name[label_name_start_position] = dic_info_label_name[position_line_start]#dict_info_label_name (position_x,position_y):label_name
        #cv2.putText(im, 'test', label_name_start_position, cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        #info_distance[position_line_start] is (distance_x,distance_y)
        #position_line_start is the start point 
    im_pil=Image.fromarray(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
    font = ImageFont.truetype('Alibaba-PuHuiTi-Regular.otf',22)
    for position_label_name in info_label_name:
        label_str = info_label_name[position_label_name]
        # str = str.encode('utf8')
        draw = ImageDraw.Draw(im_pil)
        draw.text(position_label_name, label_str, font=font, fill=(255, 0, 0))
        im_show = cv2.cvtColor(np.asarray(im_pil),cv2.COLOR_RGB2BGR)
    return im_show