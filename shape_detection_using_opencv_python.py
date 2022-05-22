"""How to detect simple geometrical shapes using opencv."""
import numpy as np
import cv2

img = cv2.imread(r'images\someshapes.jpg')
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.waitKey(0)
cv2.destroyAllWindows()
_, thresh = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print('contours\n', contours)

i = 0
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    if i < 1:
        print('\napprox\n', approx)
        print('\nraveled approx\n', approx.ravel())
    i += 1
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 20
    if len(approx) == 3:
        cv2.putText(img, 'Triangle', (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:
        x1, y1, w, h = cv2.boundingRect(approx)
        x = x1 - 20
        y = y1 - 20
        aspectRatio = float(w)/h
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv2.putText(img, 'Square', (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
            cv2.putText(img, 'Rectangle', (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    elif len(approx) == 5:
        cv2.putText(img, 'Pentagon', (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 10:
        cv2.putText(img, 'Star', (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    else:
        cv2.putText(img, 'Circle', (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

# Wow programming is just fun mehn.... we move on!!!!
# epsilon is the parameter specifying the approximation accuracy

cv2.imshow('shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()