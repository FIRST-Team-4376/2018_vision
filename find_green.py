# from transform import four_point_transform
import numpy as np
import argparse
import cv2



hmin = 58
hmax = 94

smin = 44
smax = 255

vmin = 20
vmax = 255

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,320);
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240);

hsv_min = np.array([hmin,smin,vmin])
hsv_max = np.array([hmax,smax,vmax])

while(1):
  ret, img = cap.read()
  hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  mask = cv2.inRange(hsv_img, hsv_min, hsv_max)
  res = cv2.bitwise_and(img,img, mask= mask)
  cv2.imshow('frame',mask)
  cv2.imshow('frame2',img)
  k= cv2.waitKey(5)
  if k==27:
    break

cap.release()
cv2.destroyAllWindows()
