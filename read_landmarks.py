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
        for items in sorted(fnmatch.filter(files, "*.jpg")):
                img = cv2.imread(os.path.join(root, items))
                if img is not None:
                    if root == "./"+folder+"/happy":
                        images_happy.append(img)
                    elif root == "./"+folder+"/sad":
                        images_sad.append(img)
                    else:
                        print(root)


def angle_between(p0,p1,p2,image_list,image):
    try:
        v0 = np.array(p0) - np.array(p1)
        v1 = np.array(p2) - np.array(p1)
        angle = np.math.atan2(np.linalg.det([v0,v1]),np.dot(v0,v1))
        return angle #in radians
    except:
        return False
 

images_happy =[]
images_sad =[]


            


def main(images,path,out):
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
        
        
        
        
        angle63_48_67 = angle_between(point63,point48,point67,images,foto)
        #cv2.line(img,(point48[0],point48[1]),(point63[0],point63[1]),(255,0,0),thickness=-1)
        #cv2.line(img,(point48[0],point48[1]),(point67[0],point67[1]),(255,0,0),thickness=-1)
        angles1.append(angle63_48_67)

        angle33_48_63 = angle_between(point33,point48,point63,images,foto)
        #cv2.line(img,(point48[0],point48[1]),(point33[0],point33[1]),(0,255,0),thickness=-1)
        #cv2.line(img,(point48[0],point48[1]),(point63[0],point63[1]),(0,255,0),thickness=-1)
        angles2.append(angle33_48_63)

        angle31_48_54 = angle_between(point31,point48,point54,images,foto)
        #cv2.line(img,(point48[0],point48[1]),(point31[0],point31[1]),(0,0,255),thickness=-1)
        #cv2.line(img,(point48[0],point48[1]),(point54[0],point54[1]),(0,0,255),thickness=-1)
        angles3.append(angle31_48_54)

        angle48_57_54 = angle_between(point48,point57,point54,images,foto)
        #cv2.line(img,(point57[0],point57[1]),(point48[0],point48[1]),(255,255,255),thickness=-1)
        #cv2.line(img,(point57[0],point57[1]),(point54[0],point54[1]),(255,255,255),thickness=-1)
        angles4.append(angle48_57_54)

        angle31_51_35 = angle_between(point31,point51,point35,images,foto)
        #cv2.line(img,(point51[0],point51[1]),(point31[0],point31[1]),(255,0,0),thickness=-1)
        #cv2.line(img,(point51[0],point51[1]),(point35[0],point35[1]),(255,0,0),thickness=-1)
        angles5.append(angle31_51_35)

        if angle63_48_67 != False and angle33_48_63 != False and angle31_48_54 != False and angle48_57_54 != False and angle31_51_35 != False:
            angles.append(angle63_48_67)
            angles.append(angle33_48_63)
            angles.append(angle31_48_54)
            angles.append(angle48_57_54)
            angles.append(angle31_51_35)

            fotos_angles.append(angles)


            #cv2.imwrite("emotions/{}/landmarks{}.png".format(path,foto), img) #Display the frame
            print("Fotos prontas: {0}/{1}".format(foto,len(images)))
            
            fotos_arq = open('foto_{}_angles.txt'.format(path), 'w')
            break_line = " \n"        
            fotos_arq.write("Imagens {} {}".format(path,break_line))
            i=0

            for angle_list in fotos_angles:
                i+=1
                fotos_arq.write("Foto "+str(i)+break_line)
                for angle in angle_list:
                    fotos_arq.write(str(angle)+break_line)
                fotos_arq.write(str(out)+break_line)
                
                
            fotos_arq.close()

            arq = open('angles_{}.txt'.format(path), 'w')
            
            i=1
            arq.write("angles "+str(i)+break_line)
            for angle in angles1:
                arq.write(str(angle)+break_line)
            arq.write(str(out)+break_line)
                
            i+=1
            arq.write("angles "+str(i)+break_line)
            for angle in angles2:
                arq.write(str(angle)+break_line)
            arq.write(str(out)+break_line)
            
            i+=1
            arq.write("angles "+str(i)+break_line)
            for angle in angles3:
                arq.write(str(angle)+break_line)
            arq.write(str(out)+break_line)
            
            i+=1
            arq.write("angles "+str(i)+break_line)
            for angle in angles4:
                arq.write(str(angle)+break_line)
            arq.write(str(out)+break_line)
            
            i+=1
            arq.write("angles "+str(i)+break_line)
            for angle in angles5:
                arq.write(str(angle)+break_line)
            arq.write(str(out)+break_line)

            
                
            arq.close()
        else:
            print(images.index(img))

        

load_images_from_folder("emotions")

detector = dlib.get_frontal_face_detector() #Face detector
#Landmark identifier. Set the filename to whatever you named the downloaded file
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") 


main(images_happy, "happy",1)
main(images_sad, "sad",0)