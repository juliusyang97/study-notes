import sys 
sys.path.remove("/opt/ros/kinetic/lib/python2.7/dist-packages")

import cv2
vidcap = cv2.VideoCapture('vtest.avi')
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  if cv2.waitKey(10) == 27:                    
      break
  count += 1
