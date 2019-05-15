import cv2
import numpy as np
im=cv2.imread('C:\\Users\\xiepeng\\Desktop\\predictions.png',0)
im[im!=255]=0
im_2 = np.copy(im)
#im[im==255]=1
#im = np.array(im,np.uint8)
image, contours, hierarchy = cv2.findContours(im, 3, 2)
cnt = contours[0]
rect = cv2.minAreaRect(cnt)
print('rect',rect)
box = cv2.boxPoints(rect)
print('first',box)
box = np.int0(box)
print('box',box)
#[792 706] point_1 box[0]
#[134 561] point_2 box[1]
#[200 262] point_3 box[2]
#[858 407] point_4 box[3]
#############X
#
#
#         point_3  
#                    point_4
#  point_2         
#                point_1   
#
#y
cv2.drawContours(im, [box], 0, (255, 0, 0), 2)
#per 5 to clip the rect 

slope=(box[0][1]-box[1][1])/(box[0][0]-box[1][0])
#print('slope',slope)

B=box[0][1]-box[0][0]*slope
#print('B',B)
distance=(box[0]-box[1])/5
#print('last_distance',distance)
#distance[1]=distance[0]*slope
distance=np.int0(distance)
#print('end_distance',distance)
#print('distance_value:',distance)
#print('box[2]:',box[2])
#print('sum:',box[2]+distance)
box_all = {}
box_all['a']=[box[1]+distance,
box[1],
box[2],
box[2]+distance]
box_all['b']=[box[1]+distance*2,
box[1]+distance,
box[2]+distance,
box[2]+distance*2]
box_all['c']=[box[1]+distance*3,
box[1]+distance*2,
box[2]+distance*2,
box[2]+distance*3]
box_all['d']=[box[1]+distance*4,
box[1]+distance*3,
box[2]+distance*3,
box[2]+distance*4]
box_all['e']=[box[0],
box[1]+distance*4,
box[2]+distance*4,
box[3]]
print('box_all:',np.array(box_all['a']))
print('bb',tuple(box_all['a'][1]))
r=np.zeros(im.shape,dtype="uint8")
r_2=np.zeros(im.shape,dtype="uint8")
r_3=np.zeros(im.shape,dtype="uint8")
r_4=np.zeros(im.shape,dtype="uint8")
r_5=np.zeros(im.shape,dtype="uint8")
# cv2.circle(im, tuple(box[0]), 3, 255, thickness=0,lineType=8)
# cv2.circle(im, tuple(box[1]), 3, 255, thickness=0,lineType=8)
# cv2.circle(im, tuple(box[2]), 3, 255, thickness=0,lineType=8)
# cv2.circle(im, tuple(box[3]), 3, 255, thickness=0,lineType=8)
# cv2.circle(im, tuple(box_all['a'][0]), 3, 255, thickness=0,lineType=8)
cv2.drawContours(r,[np.array(box_all['a'])],0,255, -1)
cv2.drawContours(r_2,[np.array(box_all['b'])],0,255, -1)
cv2.drawContours(r_3,[np.array(box_all['c'])],0,255, -1)
cv2.drawContours(r_4,[np.array(box_all['d'])],0,255, -1)
cv2.drawContours(r_5,[np.array(box_all['e'])],0,255, -1)
result_r = cv2.bitwise_and(r, im_2)
result_r_2 = cv2.bitwise_and(r_2, im_2)
result_r_3 = cv2.bitwise_and(r_3, im_2)
result_r_4 = cv2.bitwise_and(r_4, im_2)
result_r_5 = cv2.bitwise_and(r_5, im_2)
cv2.imshow("AND_1",result_r)
cv2.imshow("AND_2",result_r_2)
cv2.imshow("AND_3",result_r_3)
cv2.imshow("AND_4",result_r_4)
cv2.imshow("AND_5",result_r_5)
cv2.imshow('bw',im)
# cv2.imshow('r',r)
# cv2.imshow('r_2',r_2)
# cv2.imshow('r_3',r_3)
# cv2.imshow('r_4',r_4)
# cv2.imshow('r_5',r_5)
def measure_width(im):
    image_r, contours_r, hierarchy_r = cv2.findContours(im, 3, 2)
    cnt_r = contours_r[0]
    rect_r = cv2.minAreaRect(cnt_r)
    box_r = cv2.boxPoints(rect_r)
    result=np.linalg.norm(box_r[0]-box_r[3])
    return result
nt_width=max(measure_width(result_r),measure_width(result_r_2),measure_width(result_r_3),measure_width(result_r_4),measure_width(result_r_5))
# result_d=np.linalg.norm(box[0]-box[3])
# result_d_t=np.linalg.norm(box[1]-box[2])
print('nt_width',nt_width)
print('result_d',result_d)
print('result_d_t',result_d_t)
cv2.waitKey(0)
cv2.destroyAllWindows()