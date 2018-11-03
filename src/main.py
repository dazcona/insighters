import os
import cv2
from csveditor import createCSV, editCSV
import time
import random

count = 0
success = True

video = cv2.VideoCapture('video1.mp4')
success,image = video.read()

createCSV()
def isTomCruise(image):
	return random.randint(0,1)

if not os.path.exists('frames'):
	os.mkdir('frames')
while success:
	start_time = time.time()
	cv2.imwrite("frames/frame%d.jpg" % count, image)
	editCSV(count,isTomCruise(image))
	success,image = video.read()
	time.sleep(1.0 - time.time() + start_time)
	print 'Read a new frame: ', success
	count += 1
