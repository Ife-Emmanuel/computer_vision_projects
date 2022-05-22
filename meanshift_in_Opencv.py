"""Using meanshift for basic object tracking."""
import numpy as np
import cv2 as cv
cap = cv.VideoCapture('videos\Car - 2165.mp4')
# take first frame of the video
ret, frame = cap.read()
cv.imshow('firstframe', frame)
h, w, c = frame.shape
print('height : ', h, ' width : ', w)
x, y, width, height = 670, 250, 64, 45
track_window = (x, y, width, height)
# set up the ROI for the tracking
roi = frame[y : y + height, x : x + width]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array([0., 60., 32.]), np.array([180., 255., 255]))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX) # all in the four lines before will give us a histogram back projected image.
# we will pass the initial location of our target object
# and the  histogram back projected image of the meanshift function
# Set up the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)
cv.imshow('roi', roi)
while (1):
    ret, frame = cap.read()
    if ret == True:
# histogram backprojected image of the mean shift function
# histogram back projection in simple words create an image of
# thesame size but of a single channel as of our input image(frame) where each pixel
# correspond to the probability of the pixel belonging to that object. i.e the output image will
# have a object of interest in more white colour compared to the remaining part of that image
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        # apply meanshift to get the new location
        ret, track_window = cv.CamShift(dst, track_window, term_crit) # CAMShift stands for continuously adoptive mean shift.
        #print(ret)
        # Draw it on the image
        pts = cv.boxPoints(ret)
        pts = np.int0(pts)
        final_image = cv.polylines(frame, [pts], True, (0, 255, 0), 2)
        print(pts)
        # x, y, w, h = track_window
        # final_image = cv.rectangle(frame, (x, y), (x + w, x + h), 255, 3)

        cv.imshow('dst', dst)
        cv.imshow('final_image', final_image)
        k = cv.waitKey(30) & 0xFF
        if k == 27:
            break
    else:
        break