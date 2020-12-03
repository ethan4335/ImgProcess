import cv2 as cv
import numpy as np


def detect_circles_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 100)
    cimage = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(cimage, cv.HOUGH_GRADIENT, 1, 20, param1=100, param2=50, minRadius=0, maxRadius=0)
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # cv.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)
        cv.circle(image, (i[0], i[1]), 1, (20, 0, 0), 2)
    cv.imshow("circles", image)



src = cv.imread("D:/Dataset/amap_traffic/amap_traffic_train_0712/000006/3.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
detect_circles_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()
