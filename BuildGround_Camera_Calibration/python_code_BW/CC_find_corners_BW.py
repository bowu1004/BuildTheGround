import numpy as np
import cv2 as cv
import glob
# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6 * 7, 3), np.float32)
objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)
# Arrays to store object points and image points from all the images.
objpoints = []  # 3d point in real world space
imgpoints = []  # 2d points in image plane.

images = glob.glob('./sample_data_from_OpenCV/*.jpg')
for fname in images:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (7, 6), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners)
        # Print current object points and image points
        # print(objp)
        # print(corners)
        # Draw and display the corners
        cv.drawChessboardCorners(img, (7, 6), corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(500)
        # cv.waitKey()
cv.destroyAllWindows()

# Calibration
retval, cameraMatrix, distCoeffs, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
# Print Properties of Camera
print(f'retval:{retval}')
print(f'camera matrix: {cameraMatrix}')
print(f'distortion coefficients: {distCoeffs}')
print(f'rotation vectors: {rvecs}')
print(f'translation vectors: {tvecs}')
# Save Calibrated Parameters
np.savetxt('retval.txt', np.array([retval]), delimiter=',')
np.savetxt('cameraMatrix.txt', cameraMatrix, delimiter=',')
np.savetxt('distCoeffs.txt', distCoeffs, delimiter=',')
rvecs_squeezed = np.squeeze(np.array(rvecs), axis=2)
np.savetxt('rotationVectors.txt', rvecs_squeezed, delimiter=',', header=str(np.array(rvecs).shape))
tvecs_squeezed = np.squeeze(np.array(tvecs), axis=2)
np.savetxt('translationVectors.txt', tvecs_squeezed, delimiter=',', header=str(np.array(tvecs).shape))


# Undistortion
img = cv.imread('./sample_data_from_OpenCV/left12.jpg')
h, w = img.shape[:2]
newcameraMatrix, roi = cv.getOptimalNewCameraMatrix(cameraMatrix, distCoeffs, (w, h), 1, (w, h))
# 1. Using cv.undistort()
# This is the easiest way. Just call the function and use ROI obtained above to crop the result.
# undistort
dst = cv.undistort(img, cameraMatrix, distCoeffs, None, newcameraMatrix)
# crop the image
x, y, w, h = roi
dst = dst[y:y + h, x:x + w]
cv.imwrite('./undistortion_images/calibresult_of_left12_M1.png', dst)

# 2. Using remapping
# This way is a little bit more difficult. First, find a mapping function from the distorted image to the undistorted image. Then use the remap function.
# undistort
mapx, mapy = cv.initUndistortRectifyMap(cameraMatrix, distCoeffs, None, newcameraMatrix, (w, h), 5)
dst = cv.remap(img, mapx, mapy, cv.INTER_LINEAR)
# crop the image
x, y, w, h = roi
dst = dst[y:y + h, x:x + w]
cv.imwrite('./undistortion_images/calibresult_of_left12_M2.png', dst)


# Evaluation the calibration
mean_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv.projectPoints(objpoints[i], rvecs[i], tvecs[i], cameraMatrix, distCoeffs)
    error = cv.norm(imgpoints[i], imgpoints2, cv.NORM_L2) / len(imgpoints2)
    mean_error += error
print("total error: {}".format(mean_error / len(objpoints)))

print('Done.')
