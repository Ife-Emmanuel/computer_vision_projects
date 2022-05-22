import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(r'C:\Users\User\PycharmProjects\OpenCVExamples\videos\Background_Subtraction_Tutorial_frame.mp4')
cv2.namedWindow('trackbars')
cv2.createTrackbar('contour_area', 'trackbars', 500, 40000, nothing)
_, frame1 = cap.read()
print(frame1.shape)
_, frame2 = cap.read()
print(frame2.shape)

while cap.isOpened():

    try:
        print('shape 1 : ', frame2.shape)
        print('shape 2 : ', frame1.shape)
        print('==============================')

        if frame1.shape != frame2.shape:
            print('shapes not thesame : ')
    except AttributeError:
        print('frame2 : ', type(frame2))
        print('frame1 : ', type(frame1))
        continue
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(gray, 20, 255, 0)
    dilated = cv2.dilate(thresh, None, iterations= 3)
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 3)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        contour_area = cv2.getTrackbarPos('contour_area', 'trackbars')
        if cv2.contourArea(contour) < contour_area:
            continue
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # cv2.drawContours(frame1, contours, contours.index(contour), (0, 255, 0), 3)
    cv2.imshow('movement detection', frame1)
    frame1 = frame2
    _, frame2 = cap.read()
    if type(frame2):
        pass
    else:
        frame2 = frame1

    k = cv2.waitKey(2) & 0xFF
    if k == ord('q'):
        break

else:
    print('Error while capturing frame')


cap.release()
cv2.destroyAllWindows()

# data visualization, computer vision, natural language processing, machine learning, deep learning

# complete mechanical engineering courses(those sent by Timothy and autocad solid work courses)
# complete web development with django, java and basically all in that writeup
# machine learning andrew ng
# deep learning in practice
# complete coursera course on web development and deep learning
# start development e-vote social and political media platform.
