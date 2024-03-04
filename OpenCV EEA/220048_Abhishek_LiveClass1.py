import cv2
import numpy as np
import matplotlib.pyplot as plt

def solve(s):

    img = cv2.imread(s, 0)
    
    fft = np.fft.fft2(img)
    fft_shift = np.fft.fftshift(fft)
    magnitude_spectrum = 20*np.log(np.abs(fft_shift))


    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()

img_path = r''
solve(img_path)
