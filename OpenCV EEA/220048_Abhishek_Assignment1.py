# libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

def hybrid(s1,s2):
    img1 =cv2.imread(s1,0)
    img2 =cv2.imread(s2,0)

    # plt.imshow(img1, cmap='gray');plt.axis('off');plt.show()
    # plt.imshow(img2, cmap='gray');plt.axis('off');plt.show()

    F1 = np.fft.fft2(img1)
    F1shift = np.fft.fftshift(F1)
    plt.imshow(np.log1p(np.abs(F1shift)), cmap='gray');plt.axis('off');plt.show()


    F2 = np.fft.fft2(img2)
    F2shift = np.fft.fftshift(F2)
    plt.imshow(np.log1p(np.abs(F2shift)), cmap='gray');plt.axis('off');plt.show()

    # LPF
    M,N = img1.shape
    H = np.zeros((M,N), dtype=np.float32)
    D0 = 30
    for u in range(M):
        for v in range(N):
            D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
            if D <= D0:
                H[u,v] = 1
            else:
                H[u,v] = 0
    plt.imshow(H, cmap='gray');plt.axis('off');plt.show()

    #IDEAL LPF
    G1shift = F1shift * H
    plt.imshow(np.log1p(np.abs(G1shift)),cmap='gray');plt.axis('off');plt.show()

    # Inverse FT
    G1 = np.fft.ifftshift(G1shift)
    g1 = np.abs(np.fft.ifft2(G1))
    plt.imshow(g1,cmap="gray");plt.axis("off");plt.show()

    # HPF
    D0 = 10
    for u in range(M):
        for v in range(N):
            D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
            if D <= D0:
                H[u,v] = 0
            else:
                H[u,v] = 1
    plt.imshow(H, cmap='gray');plt.axis('off');plt.show()
    #IDEAL HPF
    G2shift = F2shift * H
    plt.imshow(np.log1p(np.abs(G2shift)),cmap='gray');plt.axis('off');plt.show()

    # Inverse FT
    G2 = np.fft.ifftshift(G2shift)
    g2 = np.abs(np.fft.ifft2(G2))
    plt.imshow(g2,cmap="gray");plt.axis("off");plt.show()

    hybrid_img = (g1 + g2)//2
    plt.imshow(hybrid_img, cmap="gray")
    plt.axis("off")
    plt.show()


img_path1 = '600x600.jpg'
img_path2 = 'Xaviereea.jpeg'

hybrid(img_path1,img_path2)