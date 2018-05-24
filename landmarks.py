#Code adapted from van Gent, P. (2016).
# Emotion Recognition Using Facial Landmarks, Python, DLib and OpenCV. A tech blog about fun things with Python and embedded electronics.
# Retrieved from: http://www.paulvangent.com/2016/08/05/emotion-recognition-using-facial-landmarks/
#Import required modules
import cv2
import dlib
import numpy as np
import math

def angle_between(p0,p1,p2):
    try:
        v0 = np.array(p0) - np.array(p1)
        v1 = np.array(p2) - np.array(p1)
        angle = np.math.atan2(np.linalg.det([v0,v1]),np.dot(v0,v1))
        return angle #in radians
    except:
        cv2.putText(landmark, "Nenhuma face identificada", (20,450), font,fontScale*2,fontColor,lineType)
    


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

'''Figure 6.8. Visualisation of ang5 angle'''
#VECTOR1 = 51=>31
#VECTOR2 = 51=>35



    
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 0.4
fontColor = (255,255,255)
lineType = 2
#Set up some required objects
video_capture = cv2.VideoCapture(0) #Webcam object
#Change Frame Rate
#video_capture.set(cv2.cv.CV_CAP_PROP_FPS, 60)
#Change Resolution
video_capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 320);
video_capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 230);

angles=[]

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

    point31 = []
    point33 = []
    point35 = []
    point48 = []
    point51 = []
    point54 = []
    point57 = []
    point63 = []
    point67 = []

    for k,d in enumerate(detections): #For each detected face  
        shape = predictor(clahe_image, d) #Get coordinates
        for i in range(1,68): #There are 68 landmark points on each face
            if i == 31:
                point31.append(shape.part(i).x)
                point31.append(shape.part(i).y)
            if i == 33:
                point33.append(shape.part(i).x)
                point33.append(shape.part(i).y)
            if i == 35:
                point35.append(shape.part(i).x)
                point35.append(shape.part(i).y)
            if i == 48:
                point48.append(shape.part(i).x)
                point48.append(shape.part(i).y)
            if i == 51:
                point51.append(shape.part(i).x)
                point51.append(shape.part(i).y)
            if i == 54:
                point54.append(shape.part(i).x)
                point54.append(shape.part(i).y)
            if i == 57:
                point57.append(shape.part(i).x)
                point57.append(shape.part(i).y)
            if i == 63:
                point63.append(shape.part(i).x)
                point63.append(shape.part(i).y)
            if i == 67:
                point67.append(shape.part(i).x)
                point67.append(shape.part(i).y)
        
            cv2.circle(landmark, (shape.part(i).x, shape.part(i).y), 2, (0,255,0), thickness=-1) #For each point, draw a red circle with thickness2 on the original frame
            #cv2.putText(landmark, str(i), (shape.part(i).x, shape.part(i).y), font,fontScale,fontColor,lineType)
            #        fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
            #        fontScale=0.3,
            #        color=(0, 0, 255))

    angle63_48_67 = angle_between(point63,point48,point67)
    #cv2.line(landmark,(point48[0],point48[1]),(point63[0],point63[1]),(255,0,0),thickness=1)
    #cv2.line(landmark,(point48[0],point48[1]),(point67[0],point67[1]),(255,0,0),thickness=1)
    angles.append(angle63_48_67)

    angle33_48_63 = angle_between(point33,point48,point63)
    #cv2.line(landmark,(point48[0],point48[1]),(point33[0],point33[1]),(0,255,0),thickness=1)
    #cv2.line(landmark,(point48[0],point48[1]),(point63[0],point63[1]),(0,255,0),thickness=1)
    angles.append(angle33_48_63)

    angle31_48_54 = angle_between(point31,point48,point54)
    #cv2.line(landmark,(point48[0],point48[1]),(point31[0],point31[1]),(0,0,255),thickness=1)
    #cv2.line(landmark,(point48[0],point48[1]),(point54[0],point54[1]),(0,0,255),thickness=1)
    angles.append(angle31_48_54)

    angle48_57_54 = angle_between(point48,point57,point54)
    #cv2.line(landmark,(point57[0],point57[1]),(point48[0],point48[1]),(255,255,255),thickness=1)
    #cv2.line(landmark,(point57[0],point57[1]),(point54[0],point54[1]),(255,255,255),thickness=1)
    angles.append(angle48_57_54)

    angle31_51_35 = angle_between(point31,point51,point35)
    #cv2.line(landmark,(point51[0],point51[1]),(point31[0],point31[1]),(255,0,0),thickness=1)
    #cv2.line(landmark,(point51[0],point51[1]),(point35[0],point35[1]),(255,0,0),thickness=1)
    angles.append(angle31_51_35)

    #cv2.imshow("image", frame) #Display the frame
    cv2.imshow("landmark", landmark) #Display the frame
    

    if cv2.waitKey(1) & 0xFF == ord('q'): #Exit program when the user presses 'q'
        break


    
    
cv2.destroyAllWindows()