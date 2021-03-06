# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usuario.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3
from sqlite3 import Error


class Ui_Usuario(object):
        
    def MostrarUsuario(self):
        try: #se ubica todo el codigo que puede llegar a levantar una excepcion
            connection = sqlite3.connect('TiendaDreamPotion.db') #abres la base de datos para que muestre los datos
            query = "SELECT * FROM Users" #aqui vamos a mostrar todos los registros que hemos hecho
            result = connection.execute(query)
            self.tableWidget.setRowCount(0) #va a contar columnas o filas para mostrar datos
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        except Error as e: #la excepcion le decimos error y que le nombre con la letra e en vez de poner error todo el nombre
            print (e) #imprimi el error
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}") #te va a tirar el tipo de error si es class error o name error etc.
        connection.close()
        
    def InsertarUsuario(self): #esta es nuestra funcion insertar usuario pues es mas facil de codificar para no llevar muchas lineas de codigo te va unas con una funcion y el boton hace todo
        try: #es una excepcion que checa que si el codigo esta bien , si esta mal la manda a la except 
            conn = sqlite3.connect('TiendaDreamPotion.db') #para conectarlos a la base de datos
            c = conn.cursor() #ponemos un alias al cursor para no tener nombres largos pusimos una c de cursor y ejecute la sentencia de insert etc.
            
            Users = self.usuario.toPlainText() #el cuadro texto para escribir lo pones en la funcion es donde tu escribes en cuadro del qt designer
            Nombre = self.nombre.toPlainText()
            Apellidos = self.apellidos.toPlainText()
            Tipo = self.tipo.toPlainText()
            contraseña = self.password.toPlainText()
            
            c.execute("INSERT INTO Users(Id_Usuario, Nombre, Apellidos, Tipo, Password) VALUES (?,?,?,?,?)",
                      (Users, Nombre, Apellidos, Tipo, contraseña)) #aqui es donde llamas al cuadro de texto donde escribiste y se inserta los datos y se van a la base de datos
            print("Usuario Completado")  #aqui es donde sabemos que el registro del usuario esta completado
        except Error as e: #excepcion si no jala el codigo o la sintaxis esta mal viene a la parte de excepciones rapido y queremos verificar el error
            print (e) #imprimimos el error para saber que error
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")#al ultimo utilizamos un tipo de error para saber que error fue si fue de class error o name error etc.
        conn.commit() #cerramos la base de datos
        
    def eliminarusuario(self):
        try:
            conn = sqlite3.connect('TiendaDreamPotion.db')
            c = conn.cursor()
            Users = int(self.usuario.toPlainText())
            
            c.execute("DELETE FROM Users WHERE Id_Usuario="+str(Users)) #borramos todo el registro del cliente pero poniendo una una clausula where para que se cumpla condicion para que sepas que tipo de cliente vas a borrar con el id
            print("Registro De Usuario Eliminado") #para que sepamos si borramos el registro o no 
        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        conn.commit()
        
    def ModificarUsuario(self):
        try:
            conn = sqlite3.connect('TiendaDreamPotion.db')
            c = conn.cursor()
            
            Users = self.usuario.toPlainText() #el cuadro texto para escribir lo pones en la funcion
            Nombre = self.nombre.toPlainText()
            Apellidos = self.apellidos.toPlainText()
            Tipo = self.tipo.toPlainText()
            contraseña = self.password.toPlainText()
            
            c.execute("""UPDATE Users SET Id_Usuario = ?, Nombre = ?, Apellidos = ?, Tipo = ?, Password = ? WHERE Id_Usuario = ?"""
                      ,(Users, Nombre, Apellidos, Tipo, contraseña, str(Users))) #para modificar el cliente todos los campos del cliente pero con la clausula where para que tipo de cliente quieres modificar y lo que esta entre paretensis para que sepa que cuadros de qt designer va a modificar
            print("Registro De Usuario Modificado") 
        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        conn.commit()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Usuario")
        MainWindow.resize(716, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 61, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 30, 71, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(-10, 90, 91, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(-10, 120, 91, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(-10, 60, 91, 21))
        self.label_10.setObjectName("label_10")
        self.usuario = QtWidgets.QTextEdit(self.centralwidget)
        self.usuario.setGeometry(QtCore.QRect(60, 0, 401, 21))
        self.usuario.setObjectName("usuario")
        self.nombre = QtWidgets.QTextEdit(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(60, 30, 401, 21))
        self.nombre.setObjectName("nombre")
        self.apellidos = QtWidgets.QTextEdit(self.centralwidget)
        self.apellidos.setGeometry(QtCore.QRect(60, 60, 401, 21))
        self.apellidos.setObjectName("apellidos")
        self.tipo = QtWidgets.QTextEdit(self.centralwidget)
        self.tipo.setGeometry(QtCore.QRect(60, 90, 401, 21))
        self.tipo.setObjectName("tipo")
        self.password = QtWidgets.QTextEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(60, 120, 401, 21))
        self.password.setObjectName("password")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 150, 641, 311))
        self.tableWidget.setRowCount(51)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.insertar_log = QtWidgets.QPushButton(self.centralwidget)
        self.insertar_log.setGeometry(QtCore.QRect(510, 0, 91, 21))
        self.insertar_log.setObjectName("insertar_log")
        
        self.insertar_log.clicked.connect(self.InsertarUsuario) #nuestro pushbutton de qt designer lo ponemos pero mandamos a llamar la funcion de insertar usuario para cuando le
                                                                #piques al boton te registre este usuario
        
        self.modificar_u = QtWidgets.QPushButton(self.centralwidget)
        self.modificar_u.setGeometry(QtCore.QRect(510, 40, 91, 21))
        self.modificar_u.setObjectName("modificar_u")
        
        self.modificar_u.clicked.connect(self.ModificarUsuario) #Para modificar el usuario y mandamos a llamar la funcion de def que se llama ModificarUsuario
        
        self.mostrar_u = QtWidgets.QPushButton(self.centralwidget)
        self.mostrar_u.setGeometry(QtCore.QRect(510, 80, 91, 21))
        self.mostrar_u.setObjectName("mostrar_u")
        
        self.mostrar_u.clicked.connect(self.MostrarUsuario) #Para mostrar todos los registros de usuarios o todas las entradas que hicieron.
        
        self.eliminar_U = QtWidgets.QPushButton(self.centralwidget)
        self.eliminar_U.setGeometry(QtCore.QRect(510, 120, 91, 21))
        self.eliminar_U.setObjectName("eliminar_U")
        
        self.eliminar_U.clicked.connect(self.eliminarusuario) #Este boton sirve para eliminar nuestro usuario.
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 716, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.insertar_log.clicked.connect(self.usuario.clear)
        self.insertar_log.clicked.connect(self.nombre.clear)
        self.insertar_log.clicked.connect(self.apellidos.clear)
        self.insertar_log.clicked.connect(self.tipo.clear)
        self.insertar_log.clicked.connect(self.password.clear)
        self.eliminar_U.clicked.connect(self.usuario.clear)
        self.eliminar_U.clicked.connect(self.nombre.clear)
        self.eliminar_U.clicked.connect(self.apellidos.clear)
        self.eliminar_U.clicked.connect(self.tipo.clear)
        self.eliminar_U.clicked.connect(self.password.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Id_Usuario</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Nombre</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Tipo</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Password</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Apellidos</p></body></html>"))
        self.insertar_log.setText(_translate("MainWindow", "Login"))
        self.modificar_u.setText(_translate("MainWindow", "Modificar"))
        self.mostrar_u.setText(_translate("MainWindow", "Mostrar"))
        self.eliminar_U.setText(_translate("MainWindow", "Eliminar"))


