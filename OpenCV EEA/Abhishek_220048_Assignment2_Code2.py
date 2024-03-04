from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np

def rotate(img, angle):
    
    return img.rotate(angle, resample=Image.BICUBIC, expand=True)
    

def rotatedFlags():
     
    flag = generate()

    flag_0 = flag.copy()
    flag_90 = rotate(flag, 90)
    flag_180 = rotate(flag, 180)
    flag_270 = rotate(flag, 270)

    plt.figure(figsize=(8, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(flag_0)
    plt.title('Rotated 0°')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(flag_90)
    plt.title('Rotated 90°')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(flag_180)
    plt.title('Rotated 180°')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.imshow(flag_270)
    plt.title('Rotated 270°')
    plt.axis('off')

    plt.show()

def generate():
    
    image = Image.new("RGB", (600, 600), "white")
    draw = ImageDraw.Draw(image)

    
    draw.rectangle([0, 0, 600, 200], fill="#FF9933")

    draw.rectangle([0, 200, 600, 400], fill="white")

    draw.rectangle([0, 400, 600, 600], fill="#138808")

    draw.ellipse([200, 200, 400, 400], outline="#000080", width=2)

    
    for i in range(0, 360, 15):
        x = 300 + 100 * np.cos(np.radians(i))
        y = 300 + 100 * np.sin(np.radians(i))
        draw.line([300, 300, x, y], fill="#000080", width=1)

    
    return image

rotatedFlags()


