# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 15:18:38 2016

@author: tushar
"""
from PyQt4 import QtGui
import os, sys
import modular_approach 
import cv2
class PrettyWidget(QtGui.QWidget):
    
    def __init__(self):
        super(PrettyWidget, self).__init__()
        self.initUI()
        
        
    def initUI(self):
        self.setGeometry(600, 300, 400, 200)
        self.setWindowTitle('Single Browse')     
        
        btn = QtGui.QPushButton('Browse\n(SINGLE)', self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.SingleBrowse)
        btn.move(150, 100)     

        self.show()

    def SingleBrowse(self):
        print "yo"
        filePath = QtGui.QFileDialog.getOpenFileName(self, 
                                                          "~/Desktop/PyRevolution/PyQt4",
                                                      )
        print(filePath)
        img = cv2.imread(filePath)
        cv2.imshow("IMG",img)
        images ,labels=modular_approach.pat('yalefaces')
        img_path=filePath
        l,count,gray=modular_approach.recog(images,labels,img_path)
        present=modular_approach.show_ans(l,count,gray)
        print present
        
        
        print "hello"
       # cv2.imshow("hi",line)
        
def main():
    app = QtGui.QApplication(sys.argv)
    w = PrettyWidget()
    app.exec_()


if __name__ == '__main__':
    main()