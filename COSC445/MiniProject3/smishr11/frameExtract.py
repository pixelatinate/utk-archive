import cv2
vid = cv2 .VideoCapture('rottingStrawberry.mp4')
success, img = vid .read()
count = 0
while success:
  if count % 100 == 0: # write one out of 100 frames
    cv2 .imwrite ("rottingStrawberry.%d.jpg" % count, img)      
  success, img = vid .read()
  print ('Read frame: ', success)
  count += 1