# -*- coding: utf-8 -*-

#Code adapted from van Gent, P. (2016).
# Emotion Recognition Using Facial Landmarks, Python, DLib and OpenCV. A tech blog about fun things with Python and embedded electronics.
# Retrieved from: http://www.paulvangent.com/2016/08/05/emotion-recognition-using-facial-landmarks/
#Import required modules
import cv2
import dlib
import numpy as np
import math
import os
import fnmatch




def load_images_from_folder(folder):
    for root, dir, files in os.walk("./"+folder):
        for items in fnmatch.filter(files, "*.jpg"):
                img = cv2.imread(os.path.join(root, items))
                if img is not None:
                    if root == "./"+folder+"/happy":
                        images_happy.append(img)
                    elif root == "./"+folder+"/sad":
                        images_sad.append(img)
                    else:
                        print(root)


def angle_between(p0,p1,p2):
    v0 = np.array(p0) - np.array(p1)
    v1 = np.array(p2) - np.array(p1)
    angle = np.math.atan2(np.linalg.det([v0,v1]),np.dot(v0,v1))
    return angle #in radians


images_happy =[]
images_sad =[]


            


def main(images,isHappy):
    all_angles =[]
    angles1 =[]
    angles2 =[]
    angles3 =[]
    angles4 =[]
    angles5 =[]
    fotos_angles = []
    foto=0
    print("Numero de imagens = {}".format(len(images)))
    for img in images:
        angles = []
        foto += 1
        #img_black = np.zeros_like(img)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
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
                
                
                cv2.circle(img, (shape.part(i).x, shape.part(i).y), 2, (0,255,0), thickness=-1) #For each point, draw a red circle with thickness2 on the original frame
        
        
        
        if isHappy == True:
            angle63_48_67 = angle_between(point63,point48,point67)
            #cv2.line(img,(point48[0],point48[1]),(point63[0],point63[1]),(255,0,0),thickness=-1)
            #cv2.line(img,(point48[0],point48[1]),(point67[0],point67[1]),(255,0,0),thickness=-1)
            angles1.append(angle63_48_67)

            angle33_48_63 = angle_between(point33,point48,point63)
            #cv2.line(img,(point48[0],point48[1]),(point33[0],point33[1]),(0,255,0),thickness=-1)
            #cv2.line(img,(point48[0],point48[1]),(point63[0],point63[1]),(0,255,0),thickness=-1)
            angles2.append(angle33_48_63)

            angle31_48_54 = angle_between(point31,point48,point54)
            #cv2.line(img,(point48[0],point48[1]),(point31[0],point31[1]),(0,0,255),thickness=-1)
            #cv2.line(img,(point48[0],point48[1]),(point54[0],point54[1]),(0,0,255),thickness=-1)
            angles3.append(angle31_48_54)

            angle48_57_54 = angle_between(point48,point57,point54)
            #cv2.line(img,(point57[0],point57[1]),(point48[0],point48[1]),(255,255,255),thickness=-1)
            #cv2.line(img,(point57[0],point57[1]),(point54[0],point54[1]),(255,255,255),thickness=-1)
            angles4.append(angle48_57_54)

            angle31_51_35 = angle_between(point31,point51,point35)
            #cv2.line(img,(point51[0],point51[1]),(point31[0],point31[1]),(255,0,0),thickness=-1)
            #cv2.line(img,(point51[0],point51[1]),(point35[0],point35[1]),(255,0,0),thickness=-1)
            angles5.append(angle31_51_35)

            angles.append(angle63_48_67)
            angles.append(angle33_48_63)
            angles.append(angle31_48_54)
            angles.append(angle48_57_54)
            angles.append(angle31_51_35)

            fotos_angles.append(angles)


            all_angles.append(angles1)
            all_angles.append(angles2)
            all_angles.append(angles3)
            all_angles.append(angles4)
            all_angles.append(angles5)

            cv2.imwrite("emotions/happy/landmarks{0}.png".format(foto), img) #Display the frame
            print("Fotos prontas: {0}/{1}".format(foto,len(images)))
            
            fotos_arq = open('foto_happy_angles.txt', 'w')
            fotos_arq.write("Imagens Happy")
            i=0
            break_line = " \n"

            for angle_list in fotos_angles:
                i+=1
                fotos_arq.write("Foto "+str(i)+break_line)
                for angle in angle_list:
                    fotos_arq.write(str(angle)+break_line)
                
            fotos_arq.close()

            arq = open('angles_happy.txt', 'w')

            
            for i in range(0,len(all_angles)):
                arq.write("angles "+str(i)+break_line)
                for k in range(0,len(all_angles[i])):
                    angle = all_angles[i][k]
                    arq.write(str(angle)+break_line)

            
                
            arq.close()

        else:
            angle63_48_67 = angle_between(point63,point48,point67)
            #cv2.line(img,(point48[0],point48[1]),(point63[0],point63[1]),(255,0,0),thickness=-1)
            #cv2.line(img,(point48[0],point48[1]),(point67[0],point67[1]),(255,0,0),thickness=-1)
            angles1.append(angle63_48_67)

            angle33_48_63 = angle_between(point33,point48,point63)
            #cv2.line(img,(point48[0],point48[1]),(point33[0],point33[1]),(0,255,0),thickness=-1)
            #cv2.line(img,(point48[0],point48[1]),(point63[0],point63[1]),(0,255,0),thickness=-1)
            angles2.append(angle33_48_63)

            angle31_48_54 = angle_between(point31,point48,point54)
            #cv2.line(img,(point48[0],point48[1]),(point31[0],point31[1]),(0,0,255),thickness=-1)
            #cv2.line(img,(point48[0],point48[1]),(point54[0],point54[1]),(0,0,255),thickness=-1)
            angles3.append(angle31_48_54)

            angle48_57_54 = angle_between(point48,point57,point54)
            #cv2.line(img,(point57[0],point57[1]),(point48[0],point48[1]),(255,255,255),thickness=-1)
            #cv2.line(img,(point57[0],point57[1]),(point54[0],point54[1]),(255,255,255),thickness=-1)
            angles4.append(angle48_57_54)

            angle31_51_35 = angle_between(point31,point51,point35)
            #cv2.line(img,(point51[0],point51[1]),(point31[0],point31[1]),(255,0,0),thickness=-1)
            #cv2.line(img,(point51[0],point51[1]),(point35[0],point35[1]),(255,0,0),thickness=-1)
            angles5.append(angle31_51_35)

            angles.append(angle63_48_67)
            angles.append(angle33_48_63)
            angles.append(angle31_48_54)
            angles.append(angle48_57_54)
            angles.append(angle31_51_35)

            fotos_angles.append(angles)


            all_angles.append(angles1)
            all_angles.append(angles2)
            all_angles.append(angles3)
            all_angles.append(angles4)
            all_angles.append(angles5)
            cv2.imwrite("emotions/sad/landmarks{0}.png".format(foto), img) #Display the frame
            print("Fotos prontas: {0}/{1}".format(foto,len(images)))
            
            fotos_arq = open('foto_sad_angles.txt', 'w')
            fotos_arq.write("Imagens sad")
            i=0
            break_line = " \n"
            for angle_list in fotos_angles:
                i+=1
                fotos_arq.write("Foto "+str(i)+break_line)
                for angle in angle_list:
                    fotos_arq.write(str(angle)+break_line)
                
            fotos_arq.close()

            arq = open('angles_sad.txt', 'w')

            
            for i in range(0,len(all_angles)):  
                arq.write("angles "+str(i)+break_line)
                for k in range(0,len(all_angles[i])):
                    angle = all_angles[i][k]
                    arq.write(str(angle)+break_line)

                
            arq.close()
        

load_images_from_folder("emotions")

detector = dlib.get_frontal_face_detector() #Face detector
#Landmark identifier. Set the filename to whatever you named the downloaded file
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") 


main(images_happy, True)
main(images_sad, False)