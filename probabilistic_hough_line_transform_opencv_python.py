import cv2
import numpy as np

img = cv2.imread(r'images\sudoku.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
cv2.imshow('edges', edges)
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2. line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()




























"""Hough Transform : it is a popular technique to detect any shape if you can represent that shape in
mathematical form. Hough transform can detect the shape even if it is broken or distorted a bit.
Hough transform algorithm is in steps:
1. Edge detection e.g using the canny edge detection.
2. Mapping of edge points to the hough space and storage in an accumulator.
3. Interpretation of the accumulator to yield lines of infinite length. The interpretation is done by thresholding and possibly other constraints.
4. Conversion of infinite lines to finite lines."""

# computer vision, data visualization, git and github, api and jupyterlab.
# Then an online computer vision project followed by completion of an the machine learning course.