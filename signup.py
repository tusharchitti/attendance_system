# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import re
import sqlite3
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_signUp(object):
    def insertData(self):
        username = self.uname_lineEdit.text()
        email = self.email_lineEdit.text()
        password = self.password_lineEdit.text()

        connection  = sqlite3.connect("login.db")
        connection.execute("INSERT INTO USERS VALUES(?,?,?)",(username,email,password))
        connection.commit()
        connection.close()
        
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(570, 375)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 130, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        #i have added it new
      
        #it ends here
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 230, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(160, 180, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.uname_lineEdit = QtGui.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(250, 130, 141, 20))
        self.uname_lineEdit.setObjectName(_fromUtf8("uname_lineEdit"))
        self.email_lineEdit = QtGui.QLineEdit(Dialog)
        self.email_lineEdit.setGeometry(QtCore.QRect(250, 180, 141, 20))
        self.email_lineEdit.setObjectName(_fromUtf8("email_lineEdit"))
        self.password_lineEdit = QtGui.QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QtCore.QRect(250, 230, 141, 20))
        self.password_lineEdit.setObjectName(_fromUtf8("password_lineEdit"))
        self.signup_btn = QtGui.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(270, 290, 75, 23))
        self.signup_btn.setObjectName(_fromUtf8("signup_btn"))
        ########################### Event #############################3
        #self.signup_btn.clicked.connect(self.insertData)
        self.signup_btn.clicked.connect(self.signup1Check)
        ################################################################
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(150, 10, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "USERNAME", None))
        self.label_2.setText(_translate("Dialog", "PASSWORD", None))
        self.label_3.setText(_translate("Dialog", "SUBJECT TAUGHT", None))
        self.signup_btn.setText(_translate("Dialog", "Sign Up", None))
        self.label_4.setText(_translate("Dialog", "Create Account", None))
    def signup1Check(self):
        username12= self.uname_lineEdit.text()
        password = self.password_lineEdit.text()
        subject1=self.email_lineEdit.text()
        print subject1
        connection  = sqlite3.connect("login.db")
        print "ho"
        connection.commit()
        print "lo"
        g=username12
        result = connection.execute("SELECT * FROM login WHERE username= 'tusha' ")
        print "do"
        print result
        l=0
        for data in result:
            l=1
        if(l==1):
            self.showMessageBox("error","username has been alreasy taken")
        connection.close()
        connection  = sqlite3.connect("login.db")
        print "ho"
        connection.commit()
        l1=0
        result = connection.execute("SELECT * FROM subject where subject_name=subject1")
        for data in result:
            l1=1
        if(l1==1):
            self.showMessageBox("error","wrong subject chozen")
        
        connection.close()
        print "yo1"
        x = True 
        flag=0
        p=password
        while x:    
            if (len(p)<6 or len(p)>12):  
                break  
            elif not re.search("[a-z]",p):  
                break  
            elif not re.search("[0-9]",p):  
                break  
            elif not re.search("[A-Z]",p):  
                break  
            elif not re.search("[$#@]",p):  
                break  
            else:  
                print("Valid Password") 
                flag=1
                self.showMessageBox("warning","correct_password")
                x=False  
                break  
  
        if x:  
           print("Not a Valid Password")  
           self.showMessageBox("warning","incorrect_password")
        
        #print username,password 
    def showMessageBox(self,title,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_signUp()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

