# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(860, 622)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 30, 203, 285))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.nrTelValue = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.nrTelValue.setInputMask("")
        self.nrTelValue.setMaxLength(32767)
        self.nrTelValue.setObjectName("nrTelValue")
        self.gridLayout.addWidget(self.nrTelValue, 2, 1, 1, 1)
        self.nazwiskoName = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.nazwiskoName.setObjectName("nazwiskoName")
        self.gridLayout.addWidget(self.nazwiskoName, 1, 0, 1, 1)
        self.imieName = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.imieName.setObjectName("imieName")
        self.gridLayout.addWidget(self.imieName, 0, 0, 1, 1)
        self.nazwiskoValue = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.nazwiskoValue.setObjectName("nazwiskoValue")
        self.gridLayout.addWidget(self.nazwiskoValue, 1, 1, 1, 1)
        self.nrTelName = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.nrTelName.setObjectName("nrTelName")
        self.gridLayout.addWidget(self.nrTelName, 2, 0, 1, 1)
        self.imieValue = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.imieValue.setObjectName("imieValue")
        self.gridLayout.addWidget(self.imieValue, 0, 1, 1, 1)
        self.peselName = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.peselName.setObjectName("peselName")
        self.gridLayout.addWidget(self.peselName, 3, 0, 1, 1)
        self.zapisz = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.zapisz.setObjectName("zapisz")
        self.gridLayout.addWidget(self.zapisz, 5, 0, 1, 1)
        self.zapiszDoPliku = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.zapiszDoPliku.setObjectName("zapiszDoPliku")
        self.gridLayout.addWidget(self.zapiszDoPliku, 5, 1, 1, 1)
        self.umowa = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.umowa.setObjectName("umowa")
        self.gridLayout.addWidget(self.umowa, 4, 1, 1, 1)
        self.lista = QtWidgets.QListWidget(parent=self.gridLayoutWidget)
        self.lista.setObjectName("lista")
        self.gridLayout.addWidget(self.lista, 6, 1, 1, 1)
        self.peselValue = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.peselValue.setInputMask("")
        self.peselValue.setObjectName("peselValue")
        self.gridLayout.addWidget(self.peselValue, 3, 1, 1, 1)
        self.blad = QtWidgets.QLabel(parent=Dialog)
        self.blad.setGeometry(QtCore.QRect(40, 310, 181, 21))
        self.blad.setText("")
        self.blad.setObjectName("blad")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.nazwiskoName.setText(_translate("Dialog", "Nazwisko"))
        self.imieName.setText(_translate("Dialog", "Imię"))
        self.nrTelName.setText(_translate("Dialog", "Nr telefonu"))
        self.peselName.setText(_translate("Dialog", "Pesel"))
        self.zapisz.setText(_translate("Dialog", "Zapisz"))
        self.zapiszDoPliku.setText(_translate("Dialog", "Zapisz do pliku"))
        self.umowa.setText(_translate("Dialog", "Umowa o pracę"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
