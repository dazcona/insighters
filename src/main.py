import os
import cv2
from csveditor import create_csv, edit_csv
from recognize_faces_image import recognize
import time
import argparse
import random

# def isTomCruise(image):
# 	return random.randint(0, 1)

ap = argparse.ArgumentParser()
ap.add_argument("-e", "--encodings", required=True,
	help="path to serialized db of facial encodings")
ap.add_argument("-d", "--detection-method", type=str, default="cnn",
	help="face detection model to use: either `hog` or `cnn`")
args = vars(ap.parse_args())


create_csv()

count = 0
success = True
video = cv2.VideoCapture('../data/video1.mp4')
success, image = video.read()
fps = video.get(cv2.CAP_PROP_FPS)

if not os.path.exists('frames'):
	os.mkdir('frames')

while success:

	if count % int(fps) == 0:
		edit_csv(count/int(fps), recognize(args['encodings'],'/face_recon/frames/frame%d.jpg' % count,args["detection_method"],count))

	success,image = video.read()
	print 'Read a new frame: ', success
	count += 1
