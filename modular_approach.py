 # -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 11:11:18 2016

@author: tushar
"""

import numpy as np
import cv2
import os
from PIL import Image
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
recognizer = cv2.createLBPHFaceRecognizer()
"""

#how to check weather a path exists or not
if os.path.exists('yalefaces'):
    print 2
else:
    print 4
print os.listdir('')"""

images=[]
labels=[]
def pat(path1):
    image_paths = [os.path.join(path1, f) for f in os.listdir(path1) if not f.endswith('.sad') and not f.endswith('.adi')] 
    #print image_paths
    for a in image_paths:
         # print a
          im=Image.open(a).convert('L')
          image = np.array(im,'uint8')
         # print image
          nbr = int(os.path.split(a)[1].split(".")[0].replace("subject", ""))
          faces = faceCascade.detectMultiScale(image)
          #print "the faces are"
          #print faces
          for (x, y, w, h) in faces:
             images.append(image[y: y + h, x: x + w])
             labels.append(nbr)
             cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
             cv2.waitKey(50)
    cv2.waitKey(10)
    cv2.destroyAllWindows()
    return images,labels
    
#images ,labels=pat('yalefaces')
path='yalefaces'
img_path='test.jpg'
def recog(images,labels,img_path):
    recognizer.train(images, np.array(labels))
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = cv2.imread(img_path)
    gray1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    l=[]
    gray=np.array(gray1, 'uint8')
    faces = face_cascade.detectMultiScale(gray, 1.3, 3)
    m=[]
    count=0
    #print "faces are",len(faces)
    for (x,y,w,h) in faces:
        count=count+1
        m.append(x)
        m.append(y)
        m.append(w)
        m.append(h)
        img2 = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        g= img[y:y+h, x:x+w]
        l.append(m)
        m=[]
        #print "m is",m
        cv2.imshow('cropped',g)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()
    cv2.waitKey(5000)
    cv2.destroyAllWindows()   
   # print "l is "
    #print l
    #print count
    return l,count,gray
#l,count,gray=recog(images,labels,img_path)


def show_ans(l,count,gray):
    #print "count is ",count
    present=[]
    for i in range(count):
        #print(l[i][0],l[i][1],l[i][2],l[i][3])
        cv2.imshow('Recognizing Face', gray[l[i][1]:l[i][1]+l[i][3],l[i][0]:l[i][0]+l[i][2]])
        prdicted,conf= recognizer.predict(gray[l[i][1]:l[i][1]+l[i][3],l[i][0]:l[i][0]+l[i][2]])
        cv2.waitKey(5000)
        cv2.destroyAllWindows()
       # print "we predicted"
        #print prdicted
        present.append(prdicted)
       # print "accu"
        #print  conf
    return present
#pre=show_ans(l,count,gray)
#print pre
#cv2.imshow('img',img)


cv2.waitKey(0)
cv2.destroyAllWindows()
