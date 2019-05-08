#import numpy as np
#import cv2
#from os import listdir
#path_pic_origin = 'C:\\Users\\LKJ\\Desktop\\three_part\\umbilical cord\\'
#save_pic_shape =  'C:\\Users\\LKJ\\Desktop\\three_part\\umbilical cord_exchange_ttt\\'
#pic_all = listdir(path_pic_origin)
#for pic_single in pic_all:
#    img=cv2.imread(path_pic_origin+pic_single)
#    h,w,dmonsion =img.shape
#    #平移矩阵[[1,0,-100],[0,1,-12]]
#    #其中矩阵A1,3的值与A2，3的值为平移的坐标
#    M=np.array([[1,0,56],[0,1,190]],dtype=np.float32)
#    #水平和竖直 正为向右移动 向下
#    img_change=cv2.warpAffine(img,M,(h,w))
#    end_save=save_pic_shape+pic_single[:-4]+'_exchange_ttt'+'.jpg'
#    print(end_save)
#    cv2.imwrite(end_save,img_change)
#    cv2.imshow("test",img_change)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
#import numpy as np
#import cv2
#from matplotlib import pyplot as plt
#img = cv2.imread('C:\\Users\\LKJ\\Desktop\\NT.jpg',0)
## Initiate FAST object with default values
#fast = cv2.FastFeatureDetector_create(threshold=15,nonmaxSuppression=True,type=cv2.FAST_FEATURE_DETECTOR_TYPE_9_16)
## find and draw the keypoints
#kp = fast.detect(img,None)
#img2 = cv2.drawKeypoints(img, kp, None, color=(255,0,0))
## Print all default params
#print( "Threshold: {}".format(fast.getThreshold()) )
#print( "nonmaxSuppression:{}".format(fast.getNonmaxSuppression()) )
#print( "neighborhood: {}".format(fast.getType()) )
#print( "Total Keypoints with nonmaxSuppression: {}".format(len(kp)) )
#cv2.imwrite('fast_true.png',img2)
## Disable nonmaxSuppression
#fast.setNonmaxSuppression(0)
#kp = fast.detect(img,None)
#print( "Total Keypoints without nonmaxSuppression: {}".format(len(kp)) )
#img3 = cv2.drawKeypoints(img, kp, None, color=(255,0,0))
#cv2.imwrite('fast_false.png',img3)
#霍夫圆检测
import cv2 as cv
import numpy as np

def detect_circles_demo(image):
    image_gray = cv.cvtColor(image,cv.COLOR_RGB2GRAY)
    _,mask = cv.threshold(image_gray,100,150,cv.THRESH_BINARY)
    dst = cv.pyrMeanShiftFiltering(image, 10, 100)   #边缘保留滤波EPF
    cimage = cv.cvtColor(dst, cv.COLOR_RGB2GRAY)
    circles = cv.HoughCircles(mask, cv.HOUGH_GRADIENT, 1, 50, param1=50, param2=40, minRadius=0, maxRadius=0)
    circles = np.uint16(np.around(circles)) #把circles包含的圆心和半径的值变成整数
    for i in circles[0, : ]:
        if (i[2] >200) and (i[2]<230):
            cv.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)  #画圆
            print('radius:',i[2])
            cv.circle(image, (i[0], i[1]), 2, (0, 0, 255), 2)  #画圆心
            cv.imshow("circles", image)
            cv.imshow('cimage',cimage)
        else:
            continue
    cv.imshow('mask',mask)
src = cv.imread(r'C:\Users\LKJ\Desktop\three_part\ac\IM_0904.jpg')
cv.namedWindow('input_image', cv.WINDOW_NORMAL) #设置为WINDOW_NORMAL可以任意缩放
cv.imshow('input_image', src)

detect_circles_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
#import cv2
#img = cv2.imread(r'C:\Users\LKJ\.spyder-py3\watch.jpg')
#img_origin = img.copy()
#dst = cv2.pyrMeanShiftFiltering(img,30,33)
#img_g = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#dst_g = cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)
##ret,thr = cv2.threshold(dst_g,68,225,cv2.THRESH_BINARY)
#circles = cv2.HoughCircles(dst_g,cv2.HOUGH_GRADIENT,1,50,param1=40,param2=40,minRadius=0,maxRadius=0)
#print('circles',circles[0].shape)
#for single_circle in circles[0, : ]:
#    cv2.circle(dst_g,(single_circle[0],single_circle[0]),single_circle[2],(0,0,255),2)
#    cv2.imshow("circles",dst_g)
##dst = cv2.pyrMeanShiftFiltering(thr,10,100) # only 8-bit,3-channel
#cv2.imshow('img_origin',img_origin)
#cv2.imshow('dst_g',dst_g)
##cv2.imshow('thr',thr)
##cv2.imshow('dst',dst)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#import cv2
#import numpy as np  
# 
#
#original_img= cv2.imread("C:\\Users\\LKJ\\Desktop\\cut.jpg", 0)
#img = cv2.resize(original_img,None,fx=0.8, fy=0.8, 
#                 interpolation = cv2.INTER_CUBIC)
# 
#img = cv2.GaussianBlur(img,(3,3),0)
#edges = cv2.Canny(img, 50, 150, apertureSize = 3)
#lines = cv2.HoughLines(edges,1,np.pi/180,118) #这里对最后一个参数使用了经验型的值
#result = img.copy()
#for line in lines:
#	rho = line[0][0]  #第一个元素是距离rho
#	theta= line[0][1] #第二个元素是角度theta
#	print (rho)
#	print (theta)
#	if  (theta < (np.pi/4. )) or (theta > (3.*np.pi/4.0)): #垂直直线
#		pt1 = (int(rho/np.cos(theta)),0)               #该直线与第一行的交点
#		#该直线与最后一行的焦点
#		pt2 = (int((rho-result.shape[0]*np.sin(theta))/np.cos(theta)),result.shape[0])
#		cv2.line( result, pt1, pt2, (255))             # 绘制一条白线
#	else:                                                  #水平直线
#		pt1 = (0,int(rho/np.sin(theta)))               # 该直线与第一列的交点
#		#该直线与最后一列的交点
#		pt2 = (result.shape[1], int((rho-result.shape[1]*np.cos(theta))/np.sin(theta)))
#		cv2.line(result, pt1, pt2, (255), 1)           # 绘制一条直线
#
#cv2.imshow('Canny', edges )
#cv2.imshow('Result', result)
#cv2.waitKey(0)
#cv2.destroyAllWindows()














