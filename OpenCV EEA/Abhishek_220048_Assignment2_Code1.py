from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np

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

    
    plt.imshow(image)
    plt.axis('off')
    plt.show()

generate()
