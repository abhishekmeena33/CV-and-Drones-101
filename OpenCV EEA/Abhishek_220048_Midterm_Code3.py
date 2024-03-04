import cv2
import numpy as np

def colour(s):
    
    image = cv2.imread(s)
    
    lower = np.array([0, 100, 100], dtype=np.uint8)  #Lower BGR values for yellow
    upper = np.array([40, 255, 255], dtype=np.uint8) #Upper BGR values for yellow

    mask = cv2.inRange(image, lower, upper)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    finalImage = image.copy()
    cv2.drawContours(finalImage, contours, -1, (0, 0, 255), 2)

    cv2.imshow('Original Image', image)
    cv2.imshow('Color Detected Image', finalImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


path = 'Shape.jpg'
colour(path)
