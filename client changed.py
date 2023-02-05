import psycopg2


def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS clients(
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(33) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(40) NOT NULL UNIQUE);
        """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS phones(
        id_phone SERIAL PRIMARY KEY,
        client_id INT NOT NULL REFERENCES clients(id) ON DELETE CASCADE,
        phone BIGINT UNIQUE);
    """)


def add_client(conn, first_name, last_name, email, phone=None):
    with conn.cursor() as cur:
        if search_client(cur, email=email):
            return ('Клиент с таким емейлом уже есть.')
        cur.execute("""
        INSERT INTO client(first_name, last_name, email)
        VALUES(%s, %s, %s) RETURNING id;
        """, (first_name, last_name, email))

        if phone is not None:
            id_with_phone = cur.fetchone()[0]
            add_phone(cur, id_with_phone, "9657773655")


def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO phones(client_id, phone)
        VALUES (%s, %s) RETURNING phone;
        """, (client_id, phone))


def search_client(conn, first_name=None, last_name=None, email=None, phone=None):
    with conn.cursor() as cur:
        if not first_name:
            first_name = '%'
        if not last_name:
            last_name = '%'
        if not email:
            email = '%'
        if not phone:
            cur.execute("""
                SELECT id, first_name, last_name, email, phone FROM clients
                LEFT JOIN phones ON clients.id = phones.client_id
                WHERE first_name LIKE %s AND last_name LIKE %s AND
                email LIKE %s;
                """, (first_name, last_name, email))
        else:
            cur.execute("""
                SELECT id, first_name, last_name, email, phone FROM clients
                LEFT JOIN phones ON clients.id = phones.client_id
                WHERE phone = %s;
                """, (phone,))
        return cur.fetchall()


def change_client(conn, id, first_name=None, last_name=None, email=None, phones=None):
    with conn.cursor() as cur:
        cur.execute("""
        SELECT first_name, last_name, email FROM clients
        WHERE id=%s;
        """,(id,))
        id_change  = cur.fetchone()

        if id_change is None:
            return 'Такого пользователя нет'
        data_list = [first_name, last_name, email]
        for i, data in enumerate(data_list):
            if not data:
                data_list[i] = id_change[i]
        data_list.append(id)

        cur.execute("""
        UPDATE clients 
        SET first_name = %s, last_name = %s, email = %s WHERE id = %s;
        """, (data_list))

    cur.fetchall()
    return "Пользователь успешно изменен"


def delete_phone(conn, id_delete_phone, phone_for_delete):
        id_delete_phone = input("Укажите id клиента для удаления номера: ")
        phone_for_delete = input("Какой номер телефона хотите удалить: ")
        with conn.cursor() as cur:
            cur.execute("""
               DELETE FROM phone WHERE client_id=%s AND phone=%s
               """, (id_delete_phone, phone_for_delete))


def delete_client(conn, id_delete_client, last_name_delete_client):
    id_delete_client = input("Укажите id клиента которого хотите удалить: ")
    last_name_delete_client = input("Укажите фамилию клиента которого хотите удалить: ")
    with conn.cursor() as cur:
        cur.execute("""
                   DELETE FROM clients WHERE id=%s AND last_name=%s
                   """, (id_delete_client, last_name_delete_client))
    RETURNING *



with psycopg2.connect(database='client_db', user='postgres', password='1331') as conn:
    with conn.cursor() as cur:
        create_db(cur)
        add_client(cur, "Victor", "Gugo", "vigo@gmail.com")
        add_client(cur, "Arhip", "Kuingi", "arhku@mail.ru")
        add_client(cur, "Ilya", "Repin", "repka@mail.ru")
        add_client(cur, "Klod", "Mone", "eklmn@gmail.com")
        add_phone(cur, 1, "9657773890")
        add_phone(cur, 2, "9657773690")
        add_phone(cur, 3, "9657773793")
        add_phone(cur, 4, "9657773895")
        search_client()
        change_client()
        delete_phone()
        delete_client()

conn.commit()

conn.close()
