import sys
from PyQt5 import QtWidgets
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
        return ui.label.setText('Выберите действие: \n\n'
                                '1. Добавить клиента: введите id, name, phone, email\n\n'
                                '2. Удалить клиента: введите id\n\n'
                                '3. Вывести информацию о клиенте: введите id клиента\n\n'
                                '4. Вывести информацию о всех заказах клиента: введите id \n\n'
                                '5. Вывести информацию о текущих заказах клиента\n\n'
                                '6. Вывести информацию о всех клиентах\n\n'
                                '7. Вывести информацию о занятости менеджеров\n\n'
                                '8. Назначить менеджера: id клиента, id менеджера, id проекта\n\n')

    if text == "Менеджер":
        return ui.label.setText('Выберите действие:\n\n'
                                '1. Вывести информацию о своих текущих заказах: id менеджера\n\n'
                                '2. Дополнить информацию о заказе: id заказа, описание, сроки\n\n'
                                '3. Вывести информацию о занятости разработчиков: id группы\n\n'
                                '4. Назначить разработчика на заказ: id разработчика, id заказа\n\n'
                                '5. Вывести информацию о заказе: id заказа\n\n'
                                '6. Вывести информацию о всех заказах: id менеджера\n\n')

    if text == "Разработчик":
        return ui.label.setText('Выберите действие: \n\n'
                                '1. Посмотреть список текущих заказов по вашему id \n\n'
                                '2. Посмотреть информацию о заказе по id заказа')


def do_1():
    n = int(ui.lineEdit.text()[0])

    if n == 1:
        try:
            client_id = int(ui.lineEdit.text().split()[1])
            name = ui.lineEdit.text().split()[2]
            phone = int(ui.lineEdit.text().split()[3])
            email = ui.lineEdit.text().split()[4]
            client = [(client_id, name, phone, email)]
            queries.add_client(client)
            ui.listWidget.addItems(["Клиент записан"])
        except:
            ui.listWidget.addItems(["Проверьте формат введенных данных"])

    elif n == 2:
        try:
            client_id = int(ui.lineEdit.text().split()[1])
            queries.delete_client(client_id)
            ui.listWidget.addItems(["Клиент удален"])
        except:
            ui.listWidget.addItems(["Пользователь не найден"])

    elif n == 3:
        try:
            client_id = int(ui.lineEdit.text().split()[1])
            client_info = ['ID, Name, Phone, Email']
            client_info.append(' '.join(list(map(str, queries.get_client_info(client_id)))))
            ui.listWidget.addItems(client_info)
        except:
            ui.listWidget.addItems(['Пользователь не найден'])

    elif n == 4:
        try:
            result = ['Order ID, Manager ID, Description, Deadline']
            client_id = int(ui.lineEdit.text().split()[1])
            orders = queries.get_all_orders(client_id)
            for i in orders:
                result.append(' '.join(list(map(str, i))))
            ui.listWidget.addItems(result)
        except:
            ui.listWidget.addItems(['Пользователь не найден'])

    elif n == 5:
        try:
            result = ['Order ID, Manager ID, Description, Deadline']
            client_id = int(ui.lineEdit.text().split()[1])
            orders = queries.get_current_orders(client_id)
            for i in orders:
                result.append(' '.join(list(map(str, i))))
            ui.listWidget.addItems(result)
        except:
            ui.listWidget.addItems(['Пользователь не найден'])

    elif n == 6:
        try:
            result = ['ID, Name, Phone, Email']
            orders = queries.get_clients()
            for i in orders:
                result.append(' '.join(list(map(str, i))))
            ui.listWidget.addItems(result)
        except:
            pass

    elif n == 7:
        try:
            result = ['ID, Name, Busy']
            workers = queries.get_managers_busy()
            for i in workers:
                result.append(' '.join(list(map(str, i))))
            ui.listWidget.addItems(result)
        except:
            pass

    elif n == 8:
        try:
            client_id = int(ui.lineEdit.text().split()[1])
            manager_id = int(ui.lineEdit.text().split()[2])
            project_id = int(ui.lineEdit.text().split()[3])
            if manager_id < 5:
                queries.choose_manager(client_id, manager_id, project_id)
                ui.listWidget.addItems(["Менеджер проектов назначен"])
            else:
                ui.listWidget.addItems(["Неверный ID менеджера"])
        except:
            ui.listWidget.addItems(["Данные введены неверно"])

def do_2():
    n = int(ui.lineEdit.text()[0])
    if n == 1:
        try:
            manager_id = int(ui.lineEdit.text().split()[1])
            orders = queries.get_manager_tasks(manager_id)
            manager_info = ['Manager ID, Project ID, Client ID, Description, Deadlines']
            for i in orders:
                manager_info.append(' '.join(list(map(str, i))))
            ui.listWidget.addItems(manager_info)
        except:
            ui.listWidget.addItems(['Менеджер не найден'])

    elif n == 2:
        try:
            project_id = int(ui.lineEdit.text().split()[1])
            desc = str(ui.lineEdit.text().split()[2])
            time = str(ui.lineEdit.text().split()[3])
            queries.project_info(project_id, desc, time)
            ui.listWidget.addItems(['Информация о заказе успешно обновлена'])
        except:
            ui.listWidget.addItems(['Заказ не найден'])

    elif n == 3:
        try:
            group_id = int(ui.lineEdit.text().split()[1])
            developers = queries.get_developer_orders_group(group_id)
            result = ['Developer ID, Name, Busy']
            for i in developers:
                result.append(' '.join(list(map(str, i))))
            ui.listWidget.addItems(result)
        except:
            ui.listWidget.addItems(['Группа не найдена'])

    elif n == 4:
        try:
            developer_id = int(ui.lineEdit.text().split()[1])
            project_id = int(ui.lineEdit.text().split()[2])
            queries.choose_developer(developer_id, project_id)
            ui.listWidget.addItems([f'Разработчик {developer_id} успешно записан на заказ {project_id}'])
        except:
            pass

    elif n == 5:
        try:
            order_id = int(ui.lineEdit.text().split()[1])
            result = ['Project ID, Client ID, Manager ID, Description, Deadlines']
            orders = queries.get_manager_orders(order_id)
            for i in orders:
                result.append(' '.join(list(map(str, i))))
            ui.listWidget.addItems(result)
        except:
            ui.listWidget.addItems(['Неверный id проекта'])

    elif n == 6:
        try:
            manager_id = int(ui.lineEdit.text().split()[1])
            orders = queries.get_manager_all_tasks(manager_id)
            manager_info = ['Manager ID, Project ID, Client ID, Description, Deadlines']
            for i in orders:
                manager_info.append(' '.join(list(map(str, i))))
            ui.listWidget.addItems(manager_info)
        except:
            ui.listWidget.addItems(['Менеджер не найден'])


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
