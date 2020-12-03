import cv2 as cv
import numpy as np


print("--------- Python OpenCV Tutorial ---------")
src = cv.imread("D:/Dataset/amap_traffic/amap_traffic_train_0712/000006/3.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
cv.waitKey(0)

cv.destroyAllWindows()
