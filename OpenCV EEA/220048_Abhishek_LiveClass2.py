import numpy as np
import cv2 
from matplotlib import pyplot as plt


def contourEG(s):
    img = cv2.imread(s)
    cv2.imshow('Orignal',img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray,30,200)
    contours, hierarchy = cv2.findContours(edged,  
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    img_copy = img.copy()
    cv2.drawContours(img_copy, contours, 1 , (0, 255, 0), 2) 
    cv2.imshow('Contour',img_copy)
    cv2.waitKey(0)

path= r"C:\Users\DELL\OneDrive - IIT Kanpur\Desktop\OpenCV EEA\geometric-shape-names-types-definitions.png"

contourEG(path)