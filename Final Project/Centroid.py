#!/usr/bin/env python
# coding: utf-8

# In[33]:


#import packages
import glob
import os
import imutils
import cv2

#read the images from the folder
images = [cv2.imread(file) for file in glob.glob("C:/Users/cjtol/CSI4106/Pocket/*.png")]

#covert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#blur to reduce high frequency noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

#binarize the image with a threshold
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
#thresh = cv2.adaptiveThreshold(blurred,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 2)[1]

#get the rock
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)


# In[34]:



    
# compute the center of the contour
def get_contour(image): 
    for c in cnts:
        M = cv2.moments(c)
        if M["m00"] != 0:
         cX = int(M["m10"] / M["m00"])
         cY = int(M["m01"] / M["m00"])
        else:
         cX, cY = 0, 0

        #draw contour and center of shape
        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
        cv2.putText(image, "center", (cX - 20, cY - 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        cv2.imwrite(os.path.join(path , "output.png"),image)
        #display modified image
        cv2.imshow("Image", image)
    cv2.waitKey(0)


# In[ ]:




