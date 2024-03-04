import cv2
import numpy as np

def hough_line(s):
    image = cv2.imread(s)
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(grayscale_image, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi/180, threshold=100)
    houghImage = image.copy()
    

    if lines is not None:
        for line in lines:
            rho, theta = line[0]
            a, b = np.cos(theta), np.sin(theta)
            x0, y0 = a * rho, b * rho
            x1, y1 = int(x0 + 1000 * (-b)), int(y0 + 1000 * (a))
            x2, y2 = int(x0 - 1000 * (-b)), int(y0 - 1000 * (a))
            cv2.line(houghImage, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv2.imshow('Original Image',image)
    cv2.imshow('Hough Lines Image', houghImage)
    cv2.waitKey(0)
    


hough_line(r"C:\Users\DELL\OneDrive - IIT Kanpur\Desktop\OpenCV EEA\notebbok.jpg")
