import sys
import time

import livestreamer
#import numpy as np
import cv2

# Getting stream source list
streams = livestreamer.streams(sys.argv[1])

stream = streams['best']

cap = cv2.VideoCapture(stream.url)
frame = cap.read()
cap.release()
cv2.imwrite('background.png', frame[1])
