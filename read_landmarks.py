#Code adapted from van Gent, P. (2016).
# Emotion Recognition Using Facial Landmarks, Python, DLib and OpenCV. A tech blog about fun things with Python and embedded electronics.
# Retrieved from: http://www.paulvangent.com/2016/08/05/emotion-recognition-using-facial-landmarks/
#Import required modules
import cv2
import dlib
import numpy as np
import math
import os

def load_images_from_folder(folder):
    global images
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return

def dotproduct(v1, v2):
      return sum((a*b) for a, b in zip(v1, v2))

def length(v):
  return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
  return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))

images =[]


images_happy = load_images_from_folder("emotions/happy/")
images_sad = load_images_from_folder("emotions/sad/")


detector = dlib.get_frontal_face_detector() #Face detector
#Landmark identifier. Set the filename to whatever you named the downloaded file
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") 

foto=0
print("Numero de imagens = {}".format(len(images)))
for img in images:
    foto += 1
    #img_black = np.zeros_like(img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    clahe_image = clahe.apply(gray)

    detections = detector(clahe_image, 1) #Detect the faces in the image

    for k,d in enumerate(detections): #For each detected face  
        shape = predictor(clahe_image, d) #Get coordinates
        for i in range(1,68): #There are 68 landmark points on each face
            cv2.circle(img, (shape.part(i).x, shape.part(i).y), 2, (0,255,0), thickness=-1) #For each point, draw a red circle with thickness2 on the original frame
    print(foto)
    cv2.imwrite("emotions/landmarks{0}.jpg".format(foto), img) #Display the frame
    
