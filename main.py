import cv2
import numpy as np

# list down all events included in cv2
# variable called as events and inside iterate all cv2 events
# events = [i for i in dir(cv2) if 'EVENT' in i]  # dir is inbuilt method which is going to show all classes and member
# print(events)

# now creating a script to listen for mouse event
# firstofall create mouse callable function which is executed when mouse event take place
# define function and name a function click_event and it takes few arguments
# like event -> which take place when mouse is clicked and then
# its going to give x and y coordinate where we gonna click at certain position
# inside callback function define logic


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ',', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ',' + str(y)  # converting x, y coordinate in string
        cv2.putText(img, strXY, (x, y), font, 0.5, (255, 0, 45), 2)
        cv2.imshow('image', img)
    # to know bgr color of any point creating rbuttonevnt
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]  # blue is first channel thatswhy 0 is
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ',' + str(green) + ',' + str(red)
        cv2.putText(img, strBGR, (x, y), font, 0.5, (35, 40, 78), 2)
        cv2.imshow('image', img)


# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('4281809c-8d6b-4046-a339-8c7d81af7c5c.jfif')
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
