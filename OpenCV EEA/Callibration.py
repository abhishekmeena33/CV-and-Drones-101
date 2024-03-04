import cv2
import numpy as np
import glob


chessboardsize = (8,6)
frameSize = (640,480)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,30,0.001)

objp = np.zeros((chessboardsize[0]*chessboardsize[1],3),np.float32)
objp[:,:2] = np.mgrid[0:chessboardsize[0],0:chessboardsize[1]].T.reshape(-1,2)

size_of_chessboard_squares_mm = 20
objp = objp* size_of_chessboard_squares_mm

objpoints = []
imgpoints =[]

images = glob.glob('C:/Users/DELL/OneDrive - IIT Kanpur/Desktop/OpenCV EEA/images/chess*.jpg')


for image in images:

    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, chessboardsize, None)


    print(ret)
    if ret == True:

        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11,11),(-1,-1),criteria)
        imgpoints.append(corners)

        cv2.drawChessboardCorners(img, chessboardsize, corners2, ret)
        cv2.imshow('Image',gray)
        cv2.imshow('img',img)
        cv2.waitKey(0)


cv2.destroyAllWindows()

ret, cameraMatrix, distortionCoeffs, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

print("Camera Matrix",cameraMatrix)
print("Distortion Coefficient",distortionCoeffs)


