import cv2
import numpy as np

def shape(s):
    image = cv2.imread(s)
    img = image.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    edges = cv2.Canny(blur, 30, 150)
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    shape_info = []

    for contour in contours:
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        vertices = len(approx)

        if vertices == 3:
            shape_name = "Triangle"
        elif vertices == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)
            shape_name = "Square" if 0.95 <= ar <= 1.05 else "Rectangle"
        elif vertices == 5:
            shape_name = "Pentagon"
        elif cv2.isContourConvex(approx):
            shape_name = "Circle"
        else:
            shape_name = "Triangle"

        shape_info.append({'contour': approx, 'name': shape_name})

    
    shape_info.sort(key=lambda x: cv2.contourArea(x['contour']), reverse=True)

    
    for i, info in enumerate(shape_info):
        cv2.drawContours(img, [info['contour']], 0, (0, 255, 0), 2)

        M = cv2.moments(info['contour'])
        cx, cy = int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])

        if i < 2:  
            cv2.circle(img, (cx, cy), 4, (0, 0, 0), -1)
            cv2.putText(img, f"{i+1}-Largest", (cx-20, cy+50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255-100, 0, 0), 2)


        cv2.putText(img, f"{info['name']}", (cx-10, cy+25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    
    cv2.imshow('Input Image',image )
    cv2.imshow('Output Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


shape('Window.jpg')
