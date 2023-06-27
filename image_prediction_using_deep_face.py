# import the necessary packages
from deepface import DeepFace
# import the necessary packages
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import imutils
import argparse
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", type=str,
    default="glasses_detector_rn_face.model",
    help="path to trained glasses detector model")
args = vars(ap.parse_args())

# load the input image from disk
model = load_model(args["model"])

image = cv2.imread("image/image/lop1.jpg")
orig = image.copy()
(h, w) = image.shape[:2]

# detect faces in the image
faces = DeepFace.extract_faces(image, detector_backend='retinaface')
print(faces)
# loop over the detected faces
for face_data in faces:
    face_img = face_data['face']
    startX = face_data['facial_area']['x']
    startY = face_data['facial_area']['y']
    face_width = face_data['facial_area']['w']
    face_height = face_data['facial_area']['h']

    # convert startX and startY to integers
    startX = int(startX)
    startY = int(startY)

    # calculate the end coordinates based on the face width and height
    endX = startX + int(face_width)
    endY = startY + int(face_height)
    # ensure the bounding boxes fall within the dimensions of the frame

    
    # extract the face ROI, resize it to 224x224, and preprocess it
    face_img = image[startY:endY, startX:endX]
    face_img = cv2.resize(face_img, (256, 256))
    face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)
    face_img = face_img.astype("float") / 255.0
    face_img = np.expand_dims(face_img, axis=0)
    
    # pass the face through the model to determine if the face has glasses or not
    preds = model.predict(face_img)
    (Glasses, NoGlasses) = preds[0]
    
    # determine the class label and color
    label = "Glasses" if Glasses > NoGlasses else "No Glasses"
    color = (0, 255, 0) if label == "Glasses" else (0, 0, 255)
    
    # include the probability in the label
    label = "{}: {:.2f}%".format(label, max(Glasses, NoGlasses) * 100)
    
    # display the label and bounding box rectangle on the output frame
    cv2.putText(image, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
    cv2.rectangle(image, (startX, startY), (endX, endY), color, 2)

# show the output image
resized = imutils.resize(image, width=900)
cv2.imshow("Output", resized)
cv2.waitKey(0)






