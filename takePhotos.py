import cv2 as cv
import glob
import numpy as np
import sys
from scipy import linalg
import yaml
import os
import matplotlib as plt

if not os.path.exists('test_img_pair'):
        os.mkdir('test_img_pair')

saved_count = 0

cap0 = cv.VideoCapture(1)
cap1 = cv.VideoCapture(2)

while True:
    ret0, frame0 = cap0.read()
    ret1, frame1 = cap1.read()

    camera0_name = "camera0"
    camera1_name = "camera1"

    cv.imshow('frame0_small', frame0)
    cv.imshow('frame1_small', frame1)
    
    k = cv.waitKey(1)
        
    if k == 27:
        #if ESC is pressed at any time, the program will exit.
        quit()

    if k == 32:
        #Press spacebar to start data collection
        savename = os.path.join('test_img_pair', camera0_name + '_' + str(saved_count) + '.png')
        cv.imwrite(savename, frame0)

        savename = os.path.join('test_img_pair', camera1_name + '_' + str(saved_count) + '.png')
        cv.imwrite(savename, frame1)

        saved_count += 1

cv.destroyAllWindows()