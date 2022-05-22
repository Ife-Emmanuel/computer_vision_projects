import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('image')
img = cv2.imread(r'images\lena.jpg', 1)
blue, green, red = cv2.split(img)

# cv2.createTrackbar('G', 'image', 0, b, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.createTrackbar('R', 'image', 0, 255, nothing)
switch = 'Switch\n1 : ON--0 : OFF'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)


while True:
    #img = np.zeros((512, 512, 3), np.uint8)
    img = cv2.imread(r'images\lena.jpg', 1)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    b = cv2.getTrackbarPos('G', 'image')
    g = cv2.getTrackbarPos('B', 'image')
    r = cv2.getTrackbarPos('R', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #img[:] = 0
    else:
        text = 'Blue : ' + str(b) + '\nGreen : ' + str(g) + '\nRed : ' + str(r)
        font = cv2.FONT_HERSHEY_SIMPLEX
        blue[:] = b
        green[:] = g
        red[:] = r

        img = cv2.putText(img, text, (10, 200), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('image', img)

cv2.destroyAllWindows()
#
# import cv2
# img1 = cv2.imread(r'images\lena.jpg', 1)
# b, g, r = cv2.split(img1)
# print('b : ' + str(b) + '\ng : ' + str(g) + '\nr : ' + str(r))
# img1 = cv2.merge((b, g, r))
# img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# print('\nimage1 : ' + str(img1[100, 100]))
# print('\nimage2 : ' + str(img2[100, 100]))
#
# def mouseclicks(event, x, y, flags, img):
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     if event == cv2.EVENT_LBUTTONDOWN:
#         strxy = str(x) + ', ' + str(y)
#         cv2.putText(img1, strxy, (x, y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
#         cv2.putText(img2, strxy, (x, y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
#
#     elif event == cv2.EVENT_RBUTTONDOWN:
#         [b, g, r] = img1[x, y]
#         strbgr = str(b) + ', ' + str(g) + ', ' + str(r)
#         cv2.putText(img1, strbgr, (x, y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
#         cv2.putText(img2, strbgr, (x, y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
#
# while True:
#
#     cv2.setMouseCallback('image', mouseclicks)
#     cv2.setMouseCallback('image1', mouseclicks)
#     cv2.imshow('image2', img2)
#     cv2.imshow('image', img1)
#     k = cv2.waitKey(1) & 0xFF
#
#     if k == 27:
#         break
#
# cv2.destroyAllWindows()


# Now I want to detect mouse event on my screen



# Emmanuel see if you can use [:] instead of [b, g, r] for the representation
# of the pixel of an image.
# computer vision, machine learning, data visualization, basic web development, basic game development, deep learning


