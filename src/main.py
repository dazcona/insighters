import os
import cv2
from csveditor import create_csv, edit_csv
import time
import random

def isTomCruise(image):
	return random.randint(0, 1)

create_csv()

count = 0
success = True
video = cv2.VideoCapture('../data/clip_01.mp4')
success, image = video.read()
fps = video.get(cv2.CAP_PROP_FPS)

if not os.path.exists('frames'):
	os.mkdir('frames')

while success:
	
	if count % int(fps) == 0:
		cv2.imwrite("frames/frame%d.jpg" % count, image)
		edit_csv(count/int(fps), isTomCruise(image))
	
	success,image = video.read()
	print 'Read a new frame: ', success
	count += 1