#This code will open a window where you'll be able to draw green cicles wherever you click
#Press Escape key to exit the program

import cv2
import numpy as np

# FUNCTION:
def draw_circle(event, x, y, flags, param):
#x and y are taken care of by OpenCV --> Gives mouse position
#event --> what the mousea actually did
    
    if event==cv2.EVENT_LBUTTONDOWN:

        cv2.circle(img,(x,y), 100, (0,255,0), -1)

cv2.namedWindow(winname='drawing')

cv2.setMouseCallback('drawing', draw_circle)
#We use callbacks to connect images to event functions with OpenCV
#This allows us to directly interact with images (and later on videos)
#Here we are just passing the function directly and not calling so there aren't any parenthesis

# SHOWING IMAGE WITH OPENCV:
#write this portion first it will make things easier

img=np.zeros((512,512, 3),np.int8) #creates black image

while True:

    cv2.imshow('drawing',img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()