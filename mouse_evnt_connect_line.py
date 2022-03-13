import cv2
import numpy as np


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 10, (255, 200, 40), -1)
        points.append((x, y))
        if len(points)>=2:
            cv2.line(img, points[-1], points[-2], (255, 89, 0), 5)

        cv2.imshow('image', img)


img = cv2.imread('cat png image - Google Search.png')
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
points = []  # this empty array gonna use in function
cv2.waitKey(0)
cv2.destroyAllWindows()
