import sqlite3
import datetime


conn = sqlite3.connect("DB_IT.db")
cursor = conn.cursor()

# получение информации о клиенте по его ID
def get_client_info(client_id):
    cursor.execute(f'SELECT * FROM Client WHERE "Client ID" == {client_id};')
    result = cursor.fetchone()
    return result

# получение информации о всех заказах клиента по его ID
def get_all_orders(client_id):
    cursor.execute(f'SELECT "Project ID", "Manager ID", Description, Deadlines  FROM Project WHERE "Client ID" == {client_id} ORDER BY Deadlines ASC;')
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

# получение информации о самом свободном менеджере
def get_free_manager():
    cursor.execute('SELECT "Manager ID", Busy FROM Manager ORDER BY Busy ASC LIMIT 1;')
    result = cursor.fetchall()
    return result

