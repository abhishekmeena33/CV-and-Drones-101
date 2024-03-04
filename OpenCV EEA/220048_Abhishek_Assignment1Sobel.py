import cv2
import numpy as np
import matplotlib.pyplot as plt

def Sobel(s):
    img = cv2.imread(s, cv2.IMREAD_GRAYSCALE)
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    magnitude_normalized = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)

    plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title('Original Image')
    plt.axis('off')
    plt.subplot(1, 2, 2), plt.imshow(magnitude_normalized, cmap='gray'), plt.title('Edge-Detected Image')
    plt.axis('off')

    plt.show()

img_path = '600x600.jpg'  
Sobel(img_path)
