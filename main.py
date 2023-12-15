import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QApplication, QInputDialog, QListWidgetItem

from layout import Ui_Dialog


class MyForm(QDialog):
        def __init__(self):
            super().__init__()
            self.ui = Ui_Dialog()
            self.ui.setupUi(self)
            self.ui.zapisz.clicked.connect(self.zapisz)
            self.show()

        def zapisz(self):
            def correct():
                pesel = self.ui.peselValue.text()
                if len(pesel) == 11:
                    tab = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
                    wynik = 0
                    for i in range(10):
                        wynik = wynik + int(pesel[i]) * tab[i]
                        self.ui.lista.addItem(f'{wynik}')
                    wynik = wynik % 10
                    self.ui.lista.addItem(f'{wynik}')
                    self.ui.lista.addItem(f'{pesel[10]}')
                    if int(pesel[10]) == wynik:
                        return True
                    else:
                        self.ui.blad.setText("Niepoprawny pesel")
                else:
                    self.ui.blad.setText("Niepoprawny pesel")
            if correct():
                imie = self.ui.imieValue.text()
                nazwisko = self.ui.imieValue.text()
                self.ui.lista.addItem(f'{imie} {nazwisko}')

        def zapiszdo(self):
            def correct():
                pesel = self.ui.peselValue.text()
                if len(pesel) == 11:
                    tab = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
                    wynik = 0
                    for i in range(10):
                        wynik = wynik + int(pesel[i]) * tab[i]
                        self.ui.lista.addItem(f'{wynik}')
                    wynik = wynik % 10
                    self.ui.lista.addItem(f'{wynik}')
                    self.ui.lista.addItem(f'{pesel[10]}')
                    if int(pesel[10]) == wynik:
                        return True
                    else:
                        self.ui.blad.setText("Niepoprawny pesel")
                else:
                    self.ui.blad.setText("Niepoprawny pesel")
            if correct():
                imie = self.ui.imieValue.text()
                nazwisko = self.ui.imieValue.text()
                with open('lista.txt', 'a') as file:
                    file.write(imie + " " + nazwisko + '\n')
















if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())