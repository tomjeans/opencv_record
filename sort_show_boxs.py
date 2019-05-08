# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:15:14 2019

@author: xiepeng
"""
def show_box(all_boxs):
'''all_boxs :center points of boxes ((x1,y1),(x2,y2),(x3,y3),...(xn,yn))

''' distance_x = 20
    distance_y = 50
    box_y = []
    box_x = []
    line_points=[]
    points={}
    for single in all_boxs:
        box_y.append(single[1])#[x1,x2,x3,...]
        box_x.append(single[0])#[y1,y2,y3,...]
        points[single[0]]=single[1]
    box_y_sort=sorted(box_y)
    box_x_sort=sorted(box_x)
    if len(box_x_sort)/2 == 1:
        flag_medium = int(len(box_x_sort)/2)
        start_x_medium=box_x_sort[flag_medium]
        start_y_medium=points[medium_x]
        end_x_medium=start_x_medium
        end_y_medium=start_y_medium+distance_y
        y_medium = box_y_sort[int(len(box_y_sort)/2)]
        if start_y < y_medium:
            for counts_number in range(flag_medium-1):
                start_x=box_x[flag_medium-counts_number-1]
                start_y=points[start_x]
                end_x=start_x-distance_x
                end_y=start_y-distance
                line_points.insert(flag_medium-1,((start_x,start_y),(end_x,end_y)))
                flag_medium=flag_medium-1
        elif startt_y > y_medium:
            '''the same as the last just end_y=start_y+distance'''
        else:
            '''start_y = start_y
            end_x = start_x + or - distance'''
    else:
        ''' the same as the last'''
        