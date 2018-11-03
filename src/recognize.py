# import the necessary packages
import face_recognition
import argparse
import cv2


def recognize_face(data, image, method):

    # load the input image and convert it from BGR to RGB
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # boxes
    boxes = face_recognition.face_locations(rgb, model=method)
	
	# box encodings
    box_encodings = face_recognition.face_encodings(rgb, boxes)

    # loop over the facial embeddings
    for encoding in box_encodings:
		
		# attempt to match each face in the input image to our known encodings
		matches = face_recognition.compare_faces(data["encodings"], encoding)
		
		if any(matches):
			return 1

    return 0
