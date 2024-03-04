import cv2
import numpy as np

def detect_circles(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    Circle = image.copy()

    gray = cv2.medianBlur(gray, 5)
    rows = gray.shape[0]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                               param1=100, param2=30,
                               minRadius=50, maxRadius=100)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            
            cv2.circle(Circle, center, 1, (0, 100, 100), 3)
            
            radius = i[2]
            cv2.circle(Circle, center, radius, (255, 0, 255), 3)
    
    cv2.imshow("detected circles", Circle)
    cv2.waitKey(0)   





detect_circles('Cups.jpg')
