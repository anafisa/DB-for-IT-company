import sqlite3
import datetime


conn = sqlite3.connect("DB_IT.db")
cursor = conn.cursor()


# получение информации о клиенте по его ID
def get_client_info(client_id):
    cursor.execute(f'SELECT * FROM Client WHERE "Client ID" == {client_id};')
    result = cursor.fetchone()
    return result


# получение информации о клиенте по его ID
def get_client_info(client_id):
    cursor.execute(f'SELECT * FROM Client WHERE "Client ID" == {client_id};')
    result = cursor.fetchone()
    return result


# получение информации о всех клиентах компании
def get_clients():
    cursor.execute(f'SELECT * FROM Client;')
    result = cursor.fetchall()
    return result


# получение информации о всех заказах клиента по его ID
def get_all_orders(client_id):
    cursor.execute(f'SELECT "Project ID", "Manager ID", Description, Deadlines  FROM Project WHERE "Client ID" == {client_id} ORDER BY Deadlines ASC;')
    result = cursor.fetchall()
    return result


def get_orders(order_id):
    cursor.execute(f'SELECT "Project ID", "Manager ID", Description, Deadlines  FROM Project WHERE "Project ID" == {order_id} ORDER BY Deadlines ASC;')
    result = cursor.fetchall()
    return result


def get_manager_orders(order_id):
    cursor.execute(f'SELECT * FROM Project WHERE "Project ID" == {order_id} ;')
    result = cursor.fetchall()
    return result


# получение информации о текущих заказах
def get_current_orders(client_id):
    date = str(datetime.date.today())
    cursor.execute(f'SELECT * FROM Project WHERE "Client ID" == {client_id} AND "DEADLINES" > "{date}" ORDER BY Deadlines ASC; ')
    result = cursor.fetchall()
    return result


# получение информации о текущей занятости всех менеджеров
def get_managers_busy():
    cursor.execute('SELECT "Manager ID", Name, Busy FROM Manager ORDER BY Busy ASC;')
    result = cursor.fetchall()
    return result


# получение информации о текущих заказах менеджера
def get_manager_tasks(manager_id):
    date = str(datetime.date.today())
    cursor.execute(f'SELECT "Manager ID", "Project ID", "Client ID", "Description", "Deadlines" FROM Project WHERE "Manager ID"={manager_id} AND "DEADLINES" > "{date}" ;')
    result = cursor.fetchall()
    return result


# получение информации о всех заказах менеджера
def get_manager_all_tasks(manager_id):
    cursor.execute(f'SELECT "Manager ID", "Project ID", "Client ID", "Description", "Deadlines" FROM Project WHERE "Manager ID"={manager_id};')
    result = cursor.fetchall()
    return result


# получение информации о занятости разработчиков по группам
def get_developer_orders_group(group_id):
    cursor.execute(f'SELECT "Developer ID", "Name", "Busy" FROM "Developer" WHERE "Group ID"={group_id} ORDER BY "Busy";')
    result = cursor.fetchall()
    return result


# получение информации о самом свободном менеджере
def get_free_manager():
    cursor.execute('SELECT "Manager ID", Busy FROM Manager ORDER BY Busy ASC LIMIT 1;')
    result = cursor.fetchall()
    return result


# получение всех заказов разработчика
def get_developer_orders(developer_id):
    cursor.execute(f'SELECT "Project ID" FROM "Developer-project" WHERE "Developer ID"== {developer_id};')
    result = cursor.fetchall()
    return result


# добавление нового клиента
def add_client(client):
    cursor.executemany('INSERT INTO "Client" VALUES (?,?,?,?)', client)
    conn.commit()


# удаление клиента по его id
def delete_client(client_id):
    cursor.execute(f'DELETE FROM "Client" WHERE "Client ID"={client_id}')
    conn.commit()


def choose_manager(client_id, manager_id, project_id):
    desc = "NEW"
    time = "2100-01-01"
    project = [(project_id, client_id, manager_id, desc, time)]
    cursor.executemany('INSERT INTO Project VALUES (?,?,?,?,?)', project)
    cursor.execute(f'UPDATE Manager SET Busy = Busy+1 WHERE "Manager ID" ={manager_id}')
    conn.commit()

# UPDATE имя_таблицы
# SET столбец1 = значение1, столбец2 = значение2...., столбецN = значениеN
# WHERE [условие];

def del_manager(client_id, manager_id, project_id):
    desc = "NEW"
    time = "2100-01-01"
    project = [(project_id, client_id, manager_id, desc, time)]
    cursor.executemany('INSERT INTO Project VALUES (?,?,?,?,?)', project)
    cursor.execute(f'UPDATE Manager SET Busy = Busy+1 WHERE "Manager ID" ={manager_id}')
    conn.commit()


def delete_manager(manager_id, project_id):
    cursor.execute(f'DELETE FROM "Project" WHERE "Project ID"={project_id}')
    cursor.execute(f'UPDATE Manager SET Busy=Busy-1 WHERE "Manager ID" ={manager_id}')
    conn.commit()


def choose_developer(developer_id, project_id):
    project = [(developer_id, project_id)]
    cursor.executemany('INSERT INTO "Developer-project" VALUES (?,?)', project)
    cursor.execute(f'UPDATE Developer SET Busy=Busy+1 WHERE "Developer ID" ={developer_id}')
    conn.commit()


def project_info(project_id, desc, time):
    cursor.execute(f'UPDATE Project SET Description="{desc}", Deadlines="{time}" WHERE "Project ID" ={project_id}')
    conn.commit()

# SET name = REPLACE(name, ' ', '-');