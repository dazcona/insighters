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
# Read video
video = cv2.VideoCapture('../data/clip_02.mp4')
success, image = video.read()
# Frames per second
fps = int(video.get(cv2.CAP_PROP_FPS))

if not os.path.exists('frames'):
	os.mkdir('frames')

while success:
	
	if count % fps == 0: # every second
		# Second
		second = count / fps
		# Write frame
		cv2.imwrite("frames/frame%d.jpg" % count, image)
		# Write!
		edit_csv(second, isTomCruise(image))
	
	# Keep reading!
	success, image = video.read()
	print 'Read a new frame: ', success
	count += 1