import sys
from PyQt5 import uic, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from gui_design import Ui_Dialog
import queries




app = QtWidgets.QApplication(sys.argv)
Diolog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Diolog)
Diolog.show()



def set_role():
    text = ui.comboBox.currentText()
    if text == "Администратор":
        return ui.label.setText('Выберите действие: \n \n1. Добавить клиента: введите id, name, phone, email\n \n2. Вывести информацию о клиенте: введите id клиента\n \n3. Вывести информацию о всех заказах клиента: введите id \n\n4. Вывести информацию о текущих заказах клиента\n\n5. Вывести информацию о всех клиентах\n\n6. Вывести информацию о занятости менеджеров')
    if text == "Менеджер":
        return ui.label.setText('Выберите действие: \n \n1.Вывести информацию о занятости разработчиков\n \n2. Назначить разработчика на заказ: id группы\n \n3. Вывести информацию о заказе: id заказа')
    if text == "Разработчик":
        return ui.label.setText('Выберите действие: \n \n1. Посмотреть список текущих заказов по вашему id \n \n2. Посмотреть информацию о заказе по id заказа')

def do_1():
    n = int(ui.lineEdit.text()[0])
    if n == 2:
        try:
            client_id = int(ui.lineEdit.text().split()[1])
            client_info = ['ID, Name, Phone, Email']
            client_info.append(' '.join(list(map(str, queries.get_client_info(client_id)))))
            ui.listWidget.addItems(client_info)
        except:
            ui.listWidget.addItems(['Пользователь не найден'])
            print("матвей лох")

    elif n == 3:
        try:
            result = ['Order ID, Manager ID, Description, Deadline']
            client_id = int(ui.lineEdit.text().split()[1])
            orders = queries.get_all_orders(client_id)
            for i in orders:
                result.append(' '.join(list(map(str, i))))
            ui.listWidget.addItems(result)
        except:
            pass

    elif n == 4:
        try:
            result = ['Order ID, Manager ID, Description, Deadline']
            client_id = int(ui.lineEdit.text().split()[1])
            orders = queries.get_current_orders(client_id)
            for i in orders:
                result.append(' '.join(list(map(str, i))))
            ui.listWidget.addItems(result)
        except:
            pass

    elif n == 5:
        result = ['ID, Name, Phone, Email']
        orders = queries.get_clients()
        for i in orders:
            result.append(' '.join(list(map(str, i))))
        ui.listWidget.addItems(result)

    elif n == 6:
        result = ['ID, Name, Busy']
        workers = queries.get_managers_busy()
        for i in workers:
            result.append(' '.join(list(map(str, i))))
        ui.listWidget.addItems(result)


def do_2():
    n = int(ui.lineEdit.text()[0])
    if n == 2:
        try:
            client_id = int(ui.lineEdit.text().split()[1])
            client_info = ['ID, Name, Phone, Email']
            client_info.append(' '.join(list(map(str, queries.get_client_info(client_id)))))
            ui.listWidget.addItems(client_info)
        except:
            ui.listWidget.addItems(['Пользователь не найден'])

    elif n == 3:
        try:
            result = ['Order ID, Manager ID, Description, Deadline']
            client_id = int(ui.lineEdit.text().split()[1])
            orders = queries.get_all_orders(client_id)
            for i in orders:
                result.append(' '.join(list(map(str, i))))
            ui.listWidget.addItems(result)
        except:
            pass

    elif n == 4:
        result = ['ID, Name, Phone, Email']
        orders = queries.get_clients()
        for i in orders:
            result.append(' '.join(list(map(str, i))))
        ui.listWidget.addItems(result)

    elif n == 5:
        result = ['ID, Name, Busy']
        workers = queries.get_managers_busy()
        for i in workers:
            result.append(' '.join(list(map(str, i))))
        ui.listWidget.addItems(result)

def do_3():
    n = int(ui.lineEdit.text()[0])
    if n == 1:
        try:
            result = ['ID ваших заказов']
            developer_id = int(ui.lineEdit.text().split()[1])
            orders = queries.get_developer_orders(developer_id)
            for i in orders:
                result.append(' '.join(list(map(str, i))))
            ui.listWidget.addItems(result)
        except:
            pass

    elif n == 2:
        try:
            result = ['Order ID, Manager ID, Description, Deadline']
            order_id = int(ui.lineEdit.text().split()[1])
            orders = queries.get_orders(order_id)
            for i in orders:
                result.append(' '.join(list(map(str, i))))
            ui.listWidget.addItems(result)
        except:
            pass


def clear():
    ui.listWidget.clear()

    # client_id = int(ui.lineEdit.text())
    # cursor.execute(f'SELECT * FROM Client WHERE "Client ID" == {client_id};')
    # one_result = cursor.fetchall()
    # ui.label_2.setText(f'{one_result}')



def check():
    text = ui.comboBox.currentText()
    if text == "Администратор":
        print("1")
        do_1()
    elif text == "Менеджер":
        print("2")
        do_2()
    else:
        print("3")
        do_3()



ui.pushButton_2.clicked.connect(set_role)


ui.pushButton.clicked.connect(check)

ui.pushButton_3.clicked.connect(clear)


sys.exit(app.exec_())
