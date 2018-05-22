#Code adapted from van Gent, P. (2016).
# Emotion Recognition Using Facial Landmarks, Python, DLib and OpenCV. A tech blog about fun things with Python and embedded electronics.
# Retrieved from: http://www.paulvangent.com/2016/08/05/emotion-recognition-using-facial-landmarks/
#Import required modules
import cv2
import dlib
import numpy as np
import math



#VECTOR1 = 48=>54  #BOCA INTEIRA

'''Figure 6.4. Visualisation of ang1 angle.'''
#VECTOR1 = 48=>63
#VECTOR2 = 48=>67

'''Figure 6.5. Visualisation of ang2 angle'''
#VECTOR1 = 48=>63
#VECTOR2 = 48=>33

'''Figure 6.6. Visualisation of ang3 angle'''
#VECTOR1 = 48=>54
#VECTOR2 = 48=>31


'''Figure 6.7. Visualisation of ang4 angle'''
#VECTOR1 = 57=>48    #ESQUERDO
#VECTOR2 = 57=>54  #DIREITO


def dotproduct(v1, v2):
  return sum((a*b) for a, b in zip(v1, v2))

def length(v):
  return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
  return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))

    
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 0.4
fontColor = (255,255,255)
lineType = 2
#Set up some required objects
video_capture = cv2.VideoCapture(1) #Webcam object
#Change Frame Rate
#video_capture.set(cv2.cv.CV_CAP_PROP_FPS, 60)
#Change Resolution
video_capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 320);
video_capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 230);

detector = dlib.get_frontal_face_detector() #Face detector
#Landmark identifier. Set the filename to whatever you named the downloaded file
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") 
while True:
    ret, frame = video_capture.read()
    landmark = np.zeros_like(frame)
    #frame = cv2.flip(frame,180)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    clahe_image = clahe.apply(gray)

    detections = detector(clahe_image, 1) #Detect the faces in the image

    for k,d in enumerate(detections): #For each detected face  
        shape = predictor(clahe_image, d) #Get coordinates
        for i in range(1,68): #There are 68 landmark points on each face
            if i == 48 or i == 67 or i == 57 or i == 54:
                cv2.circle(landmark, (shape.part(i).x, shape.part(i).y), 2, (255,0,0), thickness=-1) #For each point, draw a red circle with thickness2 on the original frame

            else:
                cv2.circle(landmark, (shape.part(i).x, shape.part(i).y), 2, (0,255,0), thickness=-1) #For each point, draw a red circle with thickness2 on the original frame
                cv2.putText(landmark, str(i), (shape.part(i).x, shape.part(i).y), font,fontScale,fontColor,lineType)
            #cv2.putText(frame, str(i), (shape.part(i).x,shape.part(i).y),
            #        fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
            #        fontScale=0.3,
            #        color=(0, 0, 255))
    #cv2.imshow("image", frame) #Display the frame
    cv2.imshow("landmark", landmark) #Display the frame
    

    if cv2.waitKey(1) & 0xFF == ord('q'): #Exit program when the user presses 'q'
        break


    
    
cv2.destroyAllWindows()