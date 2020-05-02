# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from main import main
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.width = 220
        self.height = 300


class PandasModel(QAbstractTableModel):
    def __init__(self,data):
        QAbstractTableModel.__init__(self)
        self._data = data
    
    def rowCount(self,parent=None):
        return self._data.shape[0]

    def columnCount(self,parent=None):
        return self._data.shape[1]

    def data(self,index,role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None
    
    def headerData(self,col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 394)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.txtRend = QtWidgets.QLineEdit(self.centralwidget)
        self.txtRend.setGeometry(QtCore.QRect(270, 130, 113, 25))
        self.txtRend.setObjectName("txtRend")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 180, 131, 17))
        self.label_2.setObjectName("label_2")

        self.txtVol = QtWidgets.QLineEdit(self.centralwidget)
        self.txtVol.setGeometry(QtCore.QRect(270, 170, 113, 25))
        self.txtVol.setObjectName("txtVol")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 310, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.iniciar)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 140, 221, 17))
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 30, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(470, 270, 161, 17))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(550, 290, 81, 17))
        self.label_5.setObjectName("label_5")

        self.lblRend = QtWidgets.QLabel(self.centralwidget)
        self.lblRend.setGeometry(QtCore.QRect(640, 270, 51, 17))
        self.lblRend.setObjectName("lblRend")

        self.lblVol = QtWidgets.QLabel(self.centralwidget)
        self.lblVol.setGeometry(QtCore.QRect(640, 290, 51, 17))
        self.lblVol.setObjectName("lblVol")

        self.gridPesos = QtWidgets.QTableView(self.centralwidget)
        self.gridPesos.setGeometry(QtCore.QRect(440, 60, 256, 192))
        self.gridPesos.setObjectName("gridPesos")

        self.fechaInicio = QtWidgets.QDateEdit(self.centralwidget)
        self.fechaInicio.setGeometry(QtCore.QRect(270, 210, 110, 26))
        self.fechaInicio.setObjectName("fechaInicio")

        self.fechaFin = QtWidgets.QDateEdit(self.centralwidget)
        self.fechaFin.setGeometry(QtCore.QRect(270, 250, 110, 26))
        self.fechaFin.setObjectName("fechaFin")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(170, 215, 101, 17))
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(190, 255, 81, 17))
        self.label_9.setObjectName("label_9")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def iniciar(self):

        try:
            df, rend, vol = main(float(self.txtRend.text()),float(self.txtVol.text()),self.fechaInicio.text(), self.fechaFin.text())

            self.gridPesos.setModel(PandasModel(df))

            self.lblRend.setText(str(rend))

            self.lblVol.setText(str(vol))
        except:
            objetoApp = App()
            QMessageBox.about(objetoApp, "ERROR", "No se encontraron datos para esa combinacion de fechas/rendimiento/volatilidad")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "DOCTA CAPITAL"))

        self.label_2.setText(_translate("MainWindow", "Volatilidad máxima"))

        self.pushButton.setText(_translate("MainWindow", "Iniciar"))

        self.label.setText(_translate("MainWindow", "Rendimiento mínimo esperado"))

        self.label_3.setText(_translate("MainWindow", "FRONTERA EFICIENTE"))

        self.label_4.setText(_translate("MainWindow", "Rendimiento esperado: "))

        self.label_5.setText(_translate("MainWindow", "Volatilidad: "))

        self.lblRend.setText(_translate("MainWindow", " "))

        self.lblVol.setText(_translate("MainWindow", " "))

        self.fechaInicio.setDisplayFormat(_translate("MainWindow", "yy/MM/dd"))

        self.fechaFin.setDisplayFormat(_translate("MainWindow", "yy/MM/dd"))

        self.label_8.setText(_translate("MainWindow", "Fecha inicio: "))

        self.label_9.setText(_translate("MainWindow", "Fecha fin: "))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
