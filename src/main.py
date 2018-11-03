# USAGE
# python main.py --video ../data/clip_01.mp4 --encodings encodings.pickle --detection-method hog

import os
import cv2
import time
import argparse
import random
import pickle
from csveditor import create_csv, edit_csv
from box import create_boxes
from recognize import recognize_face

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True,
	help="path to the video")
ap.add_argument("-e", "--encodings", required=True,
	help="path to serialized db of facial encodings")
ap.add_argument("-d", "--detection-method", type=str, default="cnn",
	help="face detection model to use: either `hog` or `cnn`")
args = vars(ap.parse_args())

# Read data
# print("[INFO] loading encodings...")
data = pickle.loads(open(args['encodings'], "rb").read())

# Create CSV
create_csv()

# Read Video
success = True
video = cv2.VideoCapture(args['video'])
success, image = video.read()
# Frames per second
count = 0
fps = int(video.get(cv2.CAP_PROP_FPS))

# Frames dir
# if not os.path.exists('frames'):
# 	os.mkdir('frames')

# Loop through the frames
while success:
	
	if count % fps == 0: # every second

		# Second
		second = count / fps

		# Write frame
		# filename = os.path.join('frames', 'frame_%d.jpg' % second)
		# cv2.imwrite(filename, image)

		# Bouding Boxes
		image_boxed = create_boxes(data, image, args["detection_method"])
		filename = '../data/test/{:04d}.png'.format(second)
		cv2.imwrite(filename, image)

		# Is our subject?
		result = recognize_face(data, image, args["detection_method"])

		# Write!
		edit_csv(second, result)

	# Keep reading!
	success, image = video.read()
	# print 'Read a new frame: ', success
	count += 1
