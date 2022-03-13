import cv2
import numpy as np


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]  # blue is first channel thatswhy 0 is
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img, (x, y), 3, (255, 89, 0), -1)
        mycolorimage = np.zeros((512, 512, 3), np.uint8)
        mycolorimage[:] = [blue, green, red]
        cv2.imshow('color', mycolorimage)


img = cv2.imread('cat png image - Google Search.png')
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
points = []  # this empty array gonna use in function
cv2.waitKey(0)
cv2.destroyAllWindows()
