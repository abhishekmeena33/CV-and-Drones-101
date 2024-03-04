import cv2
import numpy as np

def undistort(s):
    distorted_img = cv2.imread(s)
    height, width = distorted_img.shape[:2]
    pattern_size = (7, 6)

    ret, corners = cv2.findChessboardCorners(distorted_img, pattern_size)

    print(ret)
    if ret:
        obj_points = np.zeros((np.prod(pattern_size), 3), dtype=np.float32)
        obj_points[:, :2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2)

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        corners = cv2.cornerSubPix(cv2.cvtColor(distorted_img, cv2.COLOR_BGR2GRAY), corners, (5, 5), (-1, -1), criteria)

        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera([obj_points], [corners], (width, height), None, None)

        undistorted_img = cv2.undistort(distorted_img, mtx, dist)

        cv2.imshow('Distorted Image', distorted_img)
        cv2.imshow("Undistorted Image", undistorted_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

undistort(r"C:\Users\DELL\OneDrive - IIT Kanpur\Desktop\OpenCV EEA\images\img4.png")
