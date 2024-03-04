import cv2
import numpy as np

def ig_filter(s):
    image = cv2.imread(s)

    brightness = 0.5
    image1 = np.clip(image * brightness, 0, 255).astype(np.uint8)

    contrast = 1.5
    image2 = cv2.convertScaleAbs(image1, alpha=contrast, beta=0)

    image3 = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)
    image3[:, :, 1] = np.clip(image3[:, :, 1] * 1.5, 0, 255).astype(np.uint8)
    
    finalImage = cv2.cvtColor(image3, cv2.COLOR_HSV2BGR)
    cv2.imshow("Original", image)
    # cv2.imshow("Brightness" , image1)
    cv2.imshow('Filtered Image', finalImage)
    # cv2.imshow('Contrast', image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


ig_filter(r"C:\Users\DELL\OneDrive - IIT Kanpur\Desktop\OpenCV EEA\mount.jpg")
