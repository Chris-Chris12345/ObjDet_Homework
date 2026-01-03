import cv2
import numpy as np

img = cv2.imread("C:\OpenCV with python\Homework 2\CirclesImage.jpg")
output = img.copy()

#Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Gaussian blur
blurred = cv2.GaussianBlur(gray, (9, 9), 2)

#HoughCircles
circles = cv2.HoughCircles(
    blurred,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=30,
    param1=100,
    param2=30,
    minRadius=10,
    maxRadius=100
)

#Draw detected circles
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        #Cricles
        cv2.circle(output, (i[0], i[1]), i[2], (0, 255, 0), 2)
        #Centers
        cv2.circle(output, (i[0], i[1]), 2, (0, 0, 255), 3)


cv2.imshow("Detected Circles", output)
cv2.waitKey(0)
cv2.destroyAllWindows()