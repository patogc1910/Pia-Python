# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventas.ui'
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


class Ui_Ventas(object):
    def mostrar(self):
        try:
            connection = sqlite3.connect('TiendaDreamPotion.db')
            query = "SELECT * FROM Ventas "
            result = connection.execute(query)
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        connection.close()
        
    def Insertar(self):
        try:
            conn = sqlite3.connect('TiendaDreamPotion.db')
            c = conn.cursor()
            
            id_Ventas = self.Id_venta.toPlainText()
            Id_usuario = self.usuario.toPlainText()
            id_Cliente = self.Id_cliente.toPlainText()
            Fecha = self.fecha_venta.toPlainText()
            Cantidad = self.cantidad.toPlainText()
            
            c.execute("INSERT INTO Ventas(Id_Ventas, Id_Usuario, Id_Cliente, Fecha_Venta, Cantidad) VALUES (?,?,?,?,?)",
                      (id_Ventas, Id_usuario, id_Cliente, Fecha, Cantidad))
            print("Registro De venta completado")
        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        conn.commit()
        
    def eliminar(self):
        try:
            conn = sqlite3.connect('TiendaDreamPotion.db')
            c = conn.cursor()
            id_Ventas = self.Id_venta.toPlainText()
            
            c.execute("DELETE FROM Ventas WHERE Id_Ventas="+str(id_Ventas))
            print("Registro De Venta Eliminado")
        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        conn.commit()
        
    def Modificar(self):
        try:
            conn = sqlite3.connect('TiendaDreamPotion.db')
            c = conn.cursor()
            
            id_Ventas = self.Id_venta.toPlainText()
            Id_usuario = self.usuario.toPlainText()
            id_Cliente = self.Id_cliente.toPlainText()
            Fecha = self.fecha_venta.toPlainText()
            Cantidad = self.cantidad.toPlainText()
            
            c.execute("""UPDATE Ventas SET Id_Ventas = ?, Id_Usuario = ?, Id_Cliente = ?, Fecha_Venta = ?, Cantidad = ?  WHERE Id_Ventas = ?""",
                      (id_Ventas, Id_usuario, id_Cliente, Fecha, Cantidad, str(id_Ventas)))
            print("Registro De Venta Modificado")
            
        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        conn.commit()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Ventas")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.label_6.setObjectName("label_6")
        self.Id_venta = QtWidgets.QTextEdit(self.centralwidget)
        self.Id_venta.setGeometry(QtCore.QRect(70, 10, 401, 21))
        self.Id_venta.setObjectName("Id_venta")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 161, 641, 271))
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 40, 61, 21))
        self.label_7.setObjectName("label_7")
        self.usuario = QtWidgets.QTextEdit(self.centralwidget)
        self.usuario.setGeometry(QtCore.QRect(70, 40, 401, 21))
        self.usuario.setObjectName("usuario")
        self.Id_cliente = QtWidgets.QTextEdit(self.centralwidget)
        self.Id_cliente.setGeometry(QtCore.QRect(70, 70, 401, 21))
        self.Id_cliente.setObjectName("Id_cliente")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(-10, 100, 91, 21))
        self.label_9.setObjectName("label_9")
        self.fecha_venta = QtWidgets.QTextEdit(self.centralwidget)
        self.fecha_venta.setGeometry(QtCore.QRect(70, 100, 401, 21))
        self.fecha_venta.setObjectName("fecha_venta")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 70, 71, 21))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(-10, 130, 91, 21))
        self.label_10.setObjectName("label_10")
        self.cantidad = QtWidgets.QTextEdit(self.centralwidget)
        self.cantidad.setGeometry(QtCore.QRect(70, 130, 401, 21))
        self.cantidad.setObjectName("cantidad")
        self.insertar_v = QtWidgets.QPushButton(self.centralwidget)
        self.insertar_v.setGeometry(QtCore.QRect(510, 10, 91, 21))
        self.insertar_v.setObjectName("insertar_v")
        
        self.insertar_v.clicked.connect(self.Insertar)
        
        self.modificar_v = QtWidgets.QPushButton(self.centralwidget)
        self.modificar_v.setGeometry(QtCore.QRect(510, 50, 91, 21))
        self.modificar_v.setObjectName("modificar_v")
        
        self.modificar_v.clicked.connect(self.Modificar)
        
        self.mostrar_v = QtWidgets.QPushButton(self.centralwidget)
        self.mostrar_v.setGeometry(QtCore.QRect(510, 90, 91, 21))
        self.mostrar_v.setObjectName("mostrar_v")
        
        self.mostrar_v.clicked.connect(self.mostrar)
        
        self.eliminar_v = QtWidgets.QPushButton(self.centralwidget)
        self.eliminar_v.setGeometry(QtCore.QRect(510, 130, 91, 21))
        self.eliminar_v.setObjectName("eliminar_v")
        
        self.eliminar_v.clicked.connect(self.eliminar)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.insertar_v.clicked.connect(self.Id_venta.clear)
        self.insertar_v.clicked.connect(self.usuario.clear)
        self.insertar_v.clicked.connect(self.Id_cliente.clear)
        self.insertar_v.clicked.connect(self.fecha_venta.clear)
        self.insertar_v.clicked.connect(self.cantidad.clear)
        self.eliminar_v.clicked.connect(self.Id_venta.clear)
        self.eliminar_v.clicked.connect(self.usuario.clear)
        self.eliminar_v.clicked.connect(self.Id_cliente.clear)
        self.eliminar_v.clicked.connect(self.fecha_venta.clear)
        self.eliminar_v.clicked.connect(self.cantidad.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Id_Ventas</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Id_Usuario</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Fecha_Venta</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Id_Cliente</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Cantidad</p></body></html>"))
        self.insertar_v.setText(_translate("MainWindow", "Insertar"))
        self.modificar_v.setText(_translate("MainWindow", "Modificar"))
        self.mostrar_v.setText(_translate("MainWindow", "Mostrar"))
        self.eliminar_v.setText(_translate("MainWindow", "Eliminar"))
