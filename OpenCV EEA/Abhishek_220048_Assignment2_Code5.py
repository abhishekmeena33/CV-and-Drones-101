import cv2
import numpy as np

def my_estimatePoseSingleMarkers(corners, marker_size, mtx, distortion):
    marker_points = np.array([[-marker_size / 2, marker_size / 2, 0],
                              [marker_size / 2, marker_size / 2, 0],
                              [marker_size / 2, -marker_size / 2, 0],
                              [-marker_size / 2, -marker_size / 2, 0]], dtype=np.float32)
    trash = []
    rvecs = []
    tvecs = []

    for c in corners:
        _, R, t, _ = cv2.solvePnPRansac(marker_points, c, mtx, distortion)
        rvecs.append(R)
        tvecs.append(t)
        trash.append(_)

    return rvecs, tvecs, trash

def markers(s):
    
    arucoDict=cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    arucoParams=cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(arucoDict, arucoParams)
    image=cv2.imread(s)
    h,w,_=image.shape
    width=1000
    height=int(width*(h/w))
    img1= image.copy()
    img=cv2.resize(image,(width,height),interpolation=cv2.INTER_CUBIC)
    height, width, _ = img1.shape
    center_x = width // 2
    center_y = height // 2
    # print(center_x,center_y)
    corners,ids,rejected=detector.detectMarkers(image)
    print(ids)
    if len(corners) > 0:
        ids = ids.flatten()
        for (markerCorner, markerID) in zip(corners, ids):
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners
            topRight = (int(topRight[0]), int(topRight[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            cv2.line(image, topLeft, topRight, (0, 255, 0), 5)
            cv2.line(image, topRight, bottomRight, (0, 255, 0), 5)
            cv2.line(image, bottomRight, bottomLeft, (0, 255, 0), 5)
            cv2.line(image, bottomLeft, topLeft, (0, 255, 0), 5)
            cX = int((topLeft[0] + bottomRight[0] + topRight[0] + bottomLeft[0]) / 4)
            cY = int((topLeft[1] + bottomLeft[1] + bottomRight[1] + topRight[1]) / 4)
            cv2.circle(image, (cX, cY), 4, (0, 0, 255), -1)

            # Pose estimation
            intrinsic_camera = np.array([[1.47818158e+03 ,0.00000000e+00, 6.07839606e+02],[0.00000000e+00 ,1.72365548e+03 ,7.85232103e+02],[0.00000000e+00 ,0.00000000e+00 ,1.00000000e+00]])
            distortion = np.array([[ 0.04952846  ,0.67016093 , 0.01697505 ,-0.01879813 ,-2.67777073]])
            corners = np.array([corners])
            rvecs, tvecs, _ = my_estimatePoseSingleMarkers(corners, 1, intrinsic_camera, distortion)

            print(tvecs)
            # Compute pose axes
            axis_length = 0.7
            axis_points = np.float32([[axis_length, 0, 0], [0, axis_length, 0], [0, 0, -axis_length]]).reshape(-1, 3)
            image_points, _ = cv2.projectPoints(axis_points, rvecs[0], tvecs[0], intrinsic_camera, distortion)
            x_axis = (int(image_points[0][0][0]), int(image_points[0][0][1]))
            y_axis = (int(image_points[1][0][0]), int(image_points[1][0][1]))
            z_axis = (int(image_points[2][0][0]), int(image_points[2][0][1]))
            
            # Draw pose axes
            cv2.line(image, (cX, cY), x_axis, (0, 255, 0), 9)
            cv2.line(image, (cX, cY), y_axis, (255, 0,0), 9)
            cv2.line(image, (cX, cY), z_axis, (0, 0, 255), 9)

            # print(cX,cY)
    
    cv2.imshow("Image",image)
    cv2.imshow("Original Image",img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


markers(r"C:\Users\DELL\OneDrive - IIT Kanpur\Desktop\OpenCV EEA\markers\chekk (2).jpg")
