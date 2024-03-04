import cv2

img = cv2.imread(r"C:\Users\DELL\OneDrive - IIT Kanpur\Desktop\OpenCV EEA\Xaviereea.jpeg")
img1= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2 = cv2.flip(img,0)
img3 = cv2.blur(img,(1000,1000))
cv2.imshow('BlurredImage',img3)
cv2.waitKey(0)


