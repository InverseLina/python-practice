import psycopg2

# encoding=utf-8
__author__ = 'Hinsteny'


def get_conn():
    conn = psycopg2.connect(database="hello_db", user="hinsteny", password="welcome", host="127.0.0.1", port="5432")
    return conn


def create_table(conn):
    cur = conn.cursor()
    cur.execute('''CREATE TABLE if not exists COMPANY
           (ID INT PRIMARY KEY     NOT NULL,
           NAME           TEXT    NOT NULL,
           AGE            INT     NOT NULL,
           ADDRESS        CHAR(50),
           SALARY         REAL);''')
    conn.commit()
    conn.close()


def insert_data(conn):
    cur = conn.cursor()
    # cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    #   VALUES (1, 'Paul', 32, 'California', 20000.00 )")
    #
    # cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    #       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")
    #
    # cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    #       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")
    #
    # cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    #       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

    # conn.commit()
    print("Records created successfully")
    conn.close()


def select_data(conn):
    '''

    :param conn:
    :return:
    '''

    cur = conn.cursor()
    cur.execute("SELECT id, name, address, salary  from COMPANY ORDER BY id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")

    print("Operation done successfully")
    conn.close()
    pass


def update_data(conn):
    cur = conn.cursor()
    cur.execute("UPDATE COMPANY set SALARY = 50000.00 where ID=1;")
    conn.commit()
    conn.close()
    select_data(get_conn())
    pass


def delete_data(conn):
    cur = conn.cursor()
    cur.execute("DELETE from COMPANY where ID=4;")
    conn.commit()
    conn.close()
    select_data(get_conn())
    pass


# Do test
if __name__ == "__main__":
    create_table(get_conn())
    insert_data(get_conn())
    select_data(get_conn())
    update_data(get_conn())
    delete_data(get_conn())

    pass
