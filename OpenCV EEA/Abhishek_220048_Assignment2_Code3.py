import cv2
import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

def rotate(img, angle):
    return img.rotate(angle, resample=Image.BICUBIC, expand=True)

def rotatedFlags():
    global flag_0, flag_90, flag_180, flag_270
    flag = generate()

    flag_0 = flag.copy()
    flag_90 = rotate(flag, 90)
    flag_180 = rotate(flag, 180)
    flag_270 = rotate(flag, 270)


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


def calculate_average_color(section):
    if not section:
        return None
    average_color = np.mean(section, axis=0)
    return tuple(average_color.astype(int))

def is_black_or_blue(color):
    threshold = 50
    return all(c < threshold for c in color)

def unskew(s):
    image = cv2.imread(s)
    
    vertical_colors = []

    for i in range(600):
        color = tuple(image[i, 299])
        if not is_black_or_blue(color) and color not in vertical_colors:
            vertical_colors.append(color)

    num_colors = len(vertical_colors)
    third = num_colors // 3

    top_section = vertical_colors[:third]
    middle_section = vertical_colors[third:2 * third]
    bottom_section = vertical_colors[2 * third:]

    avg_color_top = calculate_average_color(top_section)
    avg_color_middle = calculate_average_color(middle_section)
    avg_color_bottom = calculate_average_color(bottom_section)

    max_avg_color_top = np.argmax(avg_color_top)
    max_avg_color_middle = np.argmax(avg_color_middle)
    max_avg_color_bottom = np.argmax(avg_color_bottom)


    cv2.imshow("Image",image)

    if max_avg_color_top == 0 and max_avg_color_middle == 0 and max_avg_color_bottom == 0:
        horizontal_colors = []
        for j in range(600):
            color = tuple(image[299, j])
            if not is_black_or_blue(color) and color not in horizontal_colors:
                horizontal_colors.append(color)

        num_horizontal_colors = len(horizontal_colors)
        third_horizontal = num_horizontal_colors // 3

        left_section = horizontal_colors[:third_horizontal]
        center_section = horizontal_colors[third_horizontal:2 * third_horizontal]
        right_section = horizontal_colors[2 * third_horizontal:]

        avg_color_left = calculate_average_color(left_section)
        avg_color_center = calculate_average_color(center_section)
        avg_color_right = calculate_average_color(right_section)

        red_channel_position_horizontal = np.argmax(avg_color_left)

        
        plt.figure(figsize=(6, 6))
        if red_channel_position_horizontal == 2:
            plt.imshow(flag_90)
            plt.axis('off')
        else:
            plt.imshow(flag_270)
            plt.axis('off')
        plt.show()
    else:
        red_channel_position = np.argmax(avg_color_top)

        plt.figure(figsize=(6, 6))
        if red_channel_position == 2:
            plt.imshow(flag_0)
            plt.axis('off')
        else:
            plt.imshow(flag_180)
            plt.axis('off')

        
        plt.show()
        
            
rotatedFlags()
unskew("images/flagTest6.jpg")
