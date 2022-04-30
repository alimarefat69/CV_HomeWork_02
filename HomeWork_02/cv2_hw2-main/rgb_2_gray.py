import cv2
import numpy as np
image = cv2.imread('picture0.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('picture_gray.jpg', gray)