import cv2
import numpy as np

def detect_ellipses(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    Ellipse = image.copy()

    gray = cv2.medianBlur(gray, 5)

    
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Fit ellipses to the contours
    for contour in contours:
        if len(contour) >= 100:
            ellipse = cv2.fitEllipse(contour)
            cv2.ellipse(Ellipse, ellipse, (255, 0, 0), 2)

    cv2.imshow('Ellipses', Ellipse)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = 'Cups.jpg'
detect_ellipses(image_path)
