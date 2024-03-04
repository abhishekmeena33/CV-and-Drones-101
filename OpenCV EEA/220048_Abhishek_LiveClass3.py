import cv2

cap = cv2.VideoCapture(0)

num = 0

while True:
    
    ret, img = cap.read()

    k = cv2.waitKey(5)

    if k== 27:
        break
    elif k== ord('s'):
        cv2.imwrite('C:/Users/DELL/OneDrive - IIT Kanpur/Desktop/OpenCV EEA/images/img' + str(num) + '.png',img)
        print("YOOOO")
        num += 1

    cv2.imshow('Img',img)

cap.release()
cv2.destroyAllWindows()