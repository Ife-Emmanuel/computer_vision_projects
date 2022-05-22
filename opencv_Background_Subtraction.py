import numpy as np
import cv2 as cv
cap = cv.VideoCapture(r'videos\Background_Subtraction_Tutorial_frame.mp4')
fgbg = cv.bgsegm.createBackgroundSubtractorGMG()
# kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
#fgbg = cv.createBackgroundSubtractorKNN(detectShadows= False)

while True:
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
    # fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN)

    cv.imshow('Frame', frame)
    cv.imshow('FG Mask Frame', fgmask)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

cap.release()
cv.destroyAllWindows()

# procastination is the grave in which oportunities are being buried.