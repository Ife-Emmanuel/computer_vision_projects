

import cv2
import datetime
filename = r'Background_Subtraction_Tutorial_frame.mp4'
cap = cv2.VideoCapture(filename)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('otheroutput.avi', fourcc, 20.0, (640, 480))
print('height : ' + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('width : ' + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
# cap.set(3, 3000)
# cap.set(4, 3000)

# print('height : ' + str(cap.get(4)))
# print('width : ' + str(cap.get(3)))
while (cap.isOpened()):
    ret, frame = cap.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
    #text = 'Width : ' + str(cap.get(3)) + ' Height : ' + str(cap.get(4))
    datet = str(datetime.datetime.now())
    frame = cv2.putText(frame, datet, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

    if ret == True:
        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()