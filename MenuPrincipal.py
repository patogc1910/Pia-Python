from PyQt5 import uic, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sqlite3 #aqui importamos el sqlite que se conecta a la base de datos
from Cliente import Ui_Cliente #aqui importamos archivos bueno que paso de .ui a .py
from Juegos import Ui_Juegos
from Ventas import Ui_Ventas
from Factura import Ui_Factura
from usuario import Ui_Usuario

qtCreatorFile = "MenuDream.ui" #aqui es donde le perimite crear archivos y ejecutarlos

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.boton.clicked.connect(self.Entrar) 
        self.boton2.clicked.connect(self.Cliente)  #aqui te permite que el boton del cliente habran la ventana de cliente.
        self.boton3.clicked.connect(self.Juego)
        self.boton4.clicked.connect(self.Ventas)
        self.boton5.clicked.connect(self.facturas)
        
    def Entrar(self): #aqui creamos una funcion para llamar esa funcion con el boton del usuario para que abra la ventana
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_Usuario() #aqui donde llamamos la funcion donde importamos de ui a .py donde le pusimos de nombre Ui_login
        self.ui.setupUi(self.ventana)#aqui es donde llamamos la funcion de la ventana donde habra el mainwindow
        self.ventana.show()#aqui es donde ya muestra la ventana
        
        
    def Cliente(self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_Cliente()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        
    def Juego(self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_Juegos()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        
    def Ventas(self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_Ventas()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        
    def facturas(self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_Factura()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        
        
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_()) #es para que corra el programa con la funcion sys y donde pone la ventana de windows lista
