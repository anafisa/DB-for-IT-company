import sys, pyowm
from PyQt5 import uic, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from test import Ui_Dialog

from PyQt5.QtWidgets import QApplication
# Form, Window = uic.loadUiType("test.ui")
app = QtWidgets.QApplication(sys.argv)

Diolog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Diolog)
Diolog.show()





def get_client_info():
    client_id = int(ui.lineEdit.text())
    cursor.execute(f'SELECT * FROM Client WHERE "Client ID" == {client_id};')
    one_result = cursor.fetchall()
    ui.label.setText(f'{one_result}')

ui.pushButton.clicked.connect(get_client_info)



sys.exit(app.exec_())
