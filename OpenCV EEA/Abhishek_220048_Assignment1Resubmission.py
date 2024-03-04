import cv2
import numpy as np
import matplotlib.pyplot as plt

def hybrid(s1, s2):
    img1 = cv2.imread(s1, 0)
    img2 = cv2.imread(s2, 0)

    plt.figure(figsize=(15, 15))

    # Original Images
    plt.subplot(2, 3, 1)
    plt.imshow(img1, cmap='gray')
    plt.title('Image 1')
    plt.axis('off')

    plt.subplot(2, 3, 2)
    plt.imshow(img2, cmap='gray')
    plt.title('Image 2')
    plt.axis('off')

    # Fourier Transform of Images
    F1 = np.fft.fft2(img1)
    F1shift = np.fft.fftshift(F1)

    plt.subplot(2, 3, 4)
    plt.imshow(np.log1p(np.abs(F1shift)), cmap='gray')
    plt.title('Fourier of Image 1')
    plt.axis('off')

    F2 = np.fft.fft2(img2)
    F2shift = np.fft.fftshift(F2)

    plt.subplot(2, 3, 5)
    plt.imshow(np.log1p(np.abs(F2shift)), cmap='gray')
    plt.title('Fourier of Image 2')
    plt.axis('off')

    # LPF
    M, N = img1.shape
    H = np.zeros((M, N), dtype=np.float32)
    D0 = 30
    for u in range(M):
        for v in range(N):
            D = np.sqrt((u - M / 2) ** 2 + (v - N / 2) ** 2)
            if D <= D0:
                H[u, v] = 1
            else:
                H[u, v] = 0

    plt.subplot(2, 3, 3)
    plt.imshow(H, cmap='gray')
    plt.title('LPF Filter')
    plt.axis('off')

    # IDEAL LPF
    G1shift = F1shift * H

    plt.subplot(2, 3, 6)
    plt.imshow(np.log1p(np.abs(G1shift)), cmap='gray')
    plt.title('Fourier after LPF')
    plt.axis('off')

    # Inverse FT
    G1 = np.fft.ifftshift(G1shift)
    g1 = np.abs(np.fft.ifft2(G1))

    plt.figure(figsize=(15, 5))

    # HPF
    D0 = 10
    for u in range(M):
        for v in range(N):
            D = np.sqrt((u - M / 2) ** 2 + (v - N / 2) ** 2)
            if D <= D0:
                H[u, v] = 0
            else:
                H[u, v] = 1

    plt.subplot(1, 3, 1)
    plt.imshow(H, cmap='gray')
    plt.title('HPF Filter')
    plt.axis('off')

    # IDEAL HPF
    G2shift = F2shift * H

    plt.subplot(1, 3, 2)
    plt.imshow(np.log1p(np.abs(G2shift)), cmap='gray')
    plt.title('Fourier after HPF')
    plt.axis('off')

    # Inverse FT
    G2 = np.fft.ifftshift(G2shift)
    g2 = np.abs(np.fft.ifft2(G2))

    # Combined Hybrid Image
    hybrid_img = (g1 + g2) // 2

    plt.subplot(1, 3, 3)
    plt.imshow(hybrid_img, cmap="gray")
    plt.title('Hybrid Image')
    plt.axis('off')

    plt.show()


img_path1 = '600x600.jpg'
img_path2 = 'Xaviereea.jpeg'

hybrid(img_path1, img_path2)
