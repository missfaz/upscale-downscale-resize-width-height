# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:45:15 2020

@author: Intern
"""

import cv2
 
# read image
img = cv2.imread('plane.jpg', cv2.IMREAD_UNCHANGED)
 
# get dimensions of image
dimensions = img.shape
 
# height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
 

print('Image Height       : ',height)
print('Image Width        : ',width)
