import cv2
import numpy as np
import imutils
import random
def nothing(x):
    pass
images=["01_h.jpg","02_h.jpg","03_h.jpg","04_h.jpg","05_h.jpg","06_h.jpg",
        "07_h.jpg","08_h.jpg","09_h.jpg","10_h.jpg","11_h.jpg","12_h.jpg",
        "13_h.jpg","14_h.jpg","15_h.jpg"]
# Load an image

images=[cv2.imread(img) for img in images]
# Resize The image
images=[imutils.resize(img, width=600) for img in images]




while(1):
    stack=[]
    all=[]
    processed=[]
    i=0
    for img in images:

            contour_list=[];
            max=1000

            clone=0
            clone_crop=img.copy();
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            lower_red = np.array([5,5,5])
            upper_red = np.array([255,255,255])
            mask = cv2.inRange(img, lower_red, upper_red)

            i=12

            clone = img.copy();


            gray = cv2.cvtColor(cv2.addWeighted(clone,i/10,np.zeros(img.shape,img.dtype),0,100), cv2.COLOR_BGR2GRAY)

            #gray = cv2.medianBlur(gray,5)
            gray_threshed2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,189-i*4,2+i/5)
            gray_threshed2=cv2.bitwise_and(gray_threshed2,gray_threshed2, mask= mask)
            mask2=cv2.bitwise_not(mask)
            gray_threshed2=cv2.bitwise_or(gray_threshed2,mask2)
            bilateral_filtered_image = cv2.bilateralFilter(gray_threshed2,5, 175, 175)
            edge_detected_image = cv2.Canny(bilateral_filtered_image, 100, 1200)

            _, contours, _= cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )

            contour_list_base = []

            for contour in contours:
                contour_list_base.append(contour)

            #if(len(contour_list_base)<max and len(contour_list_base)>0):
            contour_list=contour_list_base
              #  max=len(contour_list_base)

    # Draw contours on the original image


            for i in range(len(contour_list)):
                M = cv2.moments(contour_list[i])
                if(M["m00"]==0):
                    cX=0
                    cY=0
                else:
                    cX = int(M["m10"]/M["m00"])

                    cY = int(M["m01"]/M["m00"])
                cv2.drawContours(clone, [contour_list[i]],-1, (128,128,128), 3)
                #cv2.circle(clone, (cX, cY), 7, (255, 255, 255), -1)

    # there is an outer boundary and inner boundary for each eadge, so contours double
            cv2.imshow("Orginal",img)
            cv2.imshow('Edges',clone)
            cv2.waitKey()
        #processed.append(clone)
        #processed=[imutils.resize(img, width=250) for img in processed]
        #stack_1=np.vstack((processed[:3]))
        #stack_2=np.vstack((processed[3:6]))
        #stack_3=np.vstack((processed[6:9]))
        #stack_4=np.vstack((processed[9:12]))
        #stack_5=np.vstack((processed[12:15]))
        #stack_all=np.hstack((stack_1,stack_2,stack_3,stack_4,stack_5))
        #cv2.imshow('Objects Detected_1',stack_1)
        #cv2.imshow('Objects Detected_2',stack_2)
        #cv2.imshow('Objects Detected_3',stack_3)
        #cv2.imshow('Objects Detected_4',stack_4)
        #cv2.imshow('Objects Detected_5',stack_5)
        # cv2.imshow('Eyes',stack_all);
        #cv2.waitKey()


cv2.destroyAllWindows()
