# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Juegos.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
import sys
import sqlite3
from sqlite3 import Error


class Ui_Juegos(object):
    def MostrarJuego(self): #mostramos la funcion MostrarJuego
        try: #detiene la ejecución y nos devuelve una excepción, que no es más que una señal que ha occurrido un funcionamiento no esperado o error en el programa.
            connection = sqlite3.connect('TiendaDreamPotion.db') #vamos a conectarlo a nuestra base de datos que se llama TiendaDream
            query = "SELECT * FROM Juegos" #vamos a mostrar todos los registros de juego
            result = connection.execute(query)
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        except Error as e:#nos manda a la excepcion de error
            print (e) #imprimimos el import de error de sqlite por si es un problema de sintaxis de sql
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}") #nos dice que tipo de error es
        connection.close() #cierra la base de datos
        
    def InsertarJuego(self):
        try:
            conn = sqlite3.connect('TiendaDreamPotion.db')
            c = conn.cursor()
            
            id_juego = self.id_Juego.toPlainText() #mostramos los cuadros de texto donde escribimos en el codigo que se llaman en qt designer Text edit es para que podamos escribir o si nos marca error
            Id_Cliente = self.id_cliente.toPlainText()
            Nombre = self.nombre.toPlainText()
            Genero = self.genero.toPlainText()
            Precio = self.precio.toPlainText()
            
            c.execute("INSERT INTO Juegos(Id_Juego, Id_Cliente, Nombre,  Genero, Precio) VALUES (?,?,?,?,?)",
                      (id_juego, Id_Cliente, Nombre, Genero, Precio)) #hacemos registrar juegos para eso mostramos los cuadros de text edit para que cuando escriba y se vaya directo a la base de datos
            print("Registro De Juego Insertardo")#ponemos un print para saber si esta registrando datos
        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        conn.commit()
        
    def EliminarJuego(self):
        try:
            conn = sqlite3.connect('TiendaDreamPotion.db')
            c = conn.cursor()
            id_juego = int(self.id_Juego.toPlainText())
            
            c.execute("DELETE FROM Juegos WHERE Id_Juego="+str(id_juego)) #Elimina el juego nadamas con solo poner el id_juego
            print("Registro De Juego Eliminado")
        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        conn.commit()
        
    def ModificarJuego(self):
        try:
            conn = sqlite3.connect('TiendaDreamPotion.db')
            c = conn.cursor()
            
            id_juego = self.id_Juego.toPlainText()
            Id_Cliente = self.id_cliente.toPlainText()
            Nombre = self.nombre.toPlainText()
            Genero = self.genero.toPlainText()
            Precio = self.precio.toPlainText()
            
            c.execute("""UPDATE Juegos SET Id_Juego = ?, Id_Cliente = ?, Nombre = ?, Genero = ?, Precio = ? WHERE Id_Juego = ?"""
                      ,(id_juego, Id_Cliente, Nombre, Genero, Precio, str(id_juego)))#podemos modificar todo los campos
            print("Registro De Juego Modificado")#sirve para saber cuando modificas algo
            
        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        conn.commit()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Juegos")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-30, 0, 131, 41))
        self.label.setObjectName("label")
        self.id_Juego = QtWidgets.QTextEdit(self.centralwidget)
        self.id_Juego.setGeometry(QtCore.QRect(70, 10, 301, 21))
        self.id_Juego.setObjectName("id_Juego")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, 80, 91, 41))
        self.label_2.setObjectName("label_2")
        self.nombre = QtWidgets.QTextEdit(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(70, 90, 301, 21))
        self.nombre.setObjectName("nombre")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-30, 120, 131, 41))
        self.label_3.setObjectName("label_3")
        self.genero = QtWidgets.QTextEdit(self.centralwidget)
        self.genero.setGeometry(QtCore.QRect(70, 130, 301, 21))
        self.genero.setObjectName("genero")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 131, 41))
        self.label_4.setObjectName("label_4")
        self.precio = QtWidgets.QTextEdit(self.centralwidget)
        self.precio.setGeometry(QtCore.QRect(70, 170, 301, 21))
        self.precio.setObjectName("precio")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(-40, 40, 151, 41))
        self.label_5.setObjectName("label_5")
        self.id_cliente = QtWidgets.QTextEdit(self.centralwidget)
        self.id_cliente.setGeometry(QtCore.QRect(70, 50, 301, 21))
        self.id_cliente.setObjectName("id_cliente")
        self.insertar = QtWidgets.QPushButton(self.centralwidget)
        self.insertar.setGeometry(QtCore.QRect(500, 10, 75, 23))
        self.insertar.setObjectName("insertar")
        
        self.insertar.clicked.connect(self.InsertarJuego)
        
        self.modificar = QtWidgets.QPushButton(self.centralwidget)
        self.modificar.setGeometry(QtCore.QRect(500, 50, 75, 23))
        self.modificar.setObjectName("modificar")
        
        self.modificar.clicked.connect(self.ModificarJuego)
        
        self.mostrar = QtWidgets.QPushButton(self.centralwidget)
        self.mostrar.setGeometry(QtCore.QRect(500, 90, 75, 23))
        self.mostrar.setObjectName("mostrar")
        
        self.mostrar.clicked.connect(self.MostrarJuego)
        
        self.eliminar = QtWidgets.QPushButton(self.centralwidget)
        self.eliminar.setGeometry(QtCore.QRect(500, 130, 75, 23))
        self.eliminar.setObjectName("eliminar")
        
        self.eliminar.clicked.connect(self.EliminarJuego)
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 200, 641, 251))
        self.tableWidget.setRowCount(45)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.insertar.clicked.connect(self.id_Juego.clear)
        self.insertar.clicked.connect(self.id_cliente.clear)
        self.insertar.clicked.connect(self.nombre.clear)
        self.insertar.clicked.connect(self.genero.clear)
        self.insertar.clicked.connect(self.precio.clear)
        self.eliminar.clicked.connect(self.id_Juego.clear)
        self.eliminar.clicked.connect(self.id_cliente.clear)
        self.eliminar.clicked.connect(self.nombre.clear)
        self.eliminar.clicked.connect(self.genero.clear)
        self.eliminar.clicked.connect(self.precio.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Id_Juego</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Nombre</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Genero</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Precio"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Id_Cliente</p></body></html>"))
        self.insertar.setText(_translate("MainWindow", "Insertar"))
        self.modificar.setText(_translate("MainWindow", "Modificar"))
        self.mostrar.setText(_translate("MainWindow", "Mostrar"))
        self.eliminar.setText(_translate("MainWindow", "Eliminar"))
