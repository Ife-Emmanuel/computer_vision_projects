# import numpy as np
# import cv2
#
# img = np.zeros([512, 512, 3], np.uint8)
#
# img = cv2.line(img, (0, 0), (255, 255), (147, 96, 44), 10)
# img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 10)
#
# img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 10)
# img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)
# font = cv2.FONT_HERSHEY_SIMPLEX
# img = cv2.putText(img, 'OpenCv', (10, 510), font, 4, (0, 255, 255), 10, cv2.LINE_AA)
# cv2.imshow('image', img)
# q = cv2.waitKey(0) & 0xFF
# cv2.destroyAllWindows()

import cv2
import datetime
filename = r'Background_Subtraction_Tutorial_frame.mp4'
cap = cv2.VideoCapture(filename)
out = cv2.VideoWriter()
print('width' + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('height' + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

cap.set(3, 1208)
cap.set(4, 720)

print('width' + str(cap.get(3)))
print('height' + str(cap.get(4)))


while (cap.isOpened()):
    ret, frame = cap.read()
    text = str(datetime.datetime.now())
    font = cv2.FONT_HERSHEY_SIMPLEX
    frame = cv2.putText(frame, text, (20, 510), font, 1, (255, 255, 0), 3, cv2.LINE_AA)
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()



# import numpy as np
# import cv2
#
# # events = [i for i in dir(cv2) if 'EVENT' in i]
# # print(events)
#
# def click_event(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(x, ', ', y)
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         strxy = str(x) + ', ' + str(y)
#         cv2.putText(img, strxy, (x, y), font, 1, (255, 255, 0), 2)
#         cv2.imshow('image', img)
#
# img = np.zeros([512, 512, 3], np.uint8)
# cv2.imshow('image', img)
#
# cv2.setMouseCallback('image', click_event)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#listening and get mouse event in cv2


C:\Users\User\AppData\Local\Programs\Python\Python38\python.exe C:/Users/User/PycharmProjects/OpenCVExamples/image_blending_using_pyramids_opencv_python.py
(512, 512, 3)
(512, 512, 3)
[[[ 91 126 122]
  [ 82 119 115]
  [ 87 124 120]
  ...
  [103 168 153]
  [103 168 153]
  [105 170 155]]

 [[ 87 122 118]
  [ 77 114 110]
  [ 80 117 113]
  ...
  [114 181 166]
  [116 183 168]
  [118 185 170]]

 [[ 82 117 113]
  [ 74 111 107]
  [ 78 115 111]
  ...
  [108 178 161]
  [109 180 163]
  [111 182 165]]

 ...

 [[113 157 116]
  [115 160 117]
  [120 163 120]
  ...
  [109 139  98]
  [109 141 100]
  [111 144 100]]

 [[107 151 112]
  [109 153 112]
  [112 155 112]
  ...
  [112 143  98]
  [111 144  99]
  [111 144  99]]

 [[113 157 118]
  [113 157 116]
  [117 157 116]
  ...
  [125 156 111]
  [120 154 107]
  [118 152 105]]]

Process finished with exit code -1
