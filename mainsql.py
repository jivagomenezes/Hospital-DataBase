import mysql.connector

def create_db(name: str) -> mysql.connector.cursor_cext.CMySQLCursor:
    """Esta função criar uma base de dados com o nome name"""
    # PASSO 1: Criar uma conexão
    mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    password="123456",
    )

    # PASSO 2: Criar uma Base de Dados
    c = mydb.cursor()
    c.execute(f"CREATE DATABASE IF NOT EXISTS {name}")
    print(type(c))
    return c

def check_dbases() -> tuple:
    """Esta função verifica as bases de dados existentes"""
    mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    password="123456",
    )

    cursor = mydb.cursor()
    cursor.execute("SHOW DATABASES")
    return [x for x in cursor]

def create_table(cursor, name):
    """Esta função cria uma tabela table numa base de dados db com os campos fields
    em que é gerada uma PRIMARY KEY"""
    db = mysql.connector.connect(
        host="localhost",
        user="user",
        password="123456",
        database=name
        )

    c = db.cursor()
    c.execute("CREATE TABLE users (nome VARCHAR(255), idade VARCHAR(255))")

def check_table(cursor, name):
    cursor.execute("SHOW TABLES")
    return (x for x in cursor)

def insert(name):
    my_db = mysql.connector.connect(
        host="localhost",
        user="user",
        password="123456",
        database=name
        )

    
    values = [input(f'Indique {el}: ') for el in ('nome', 'idade')]
    sql = "INSERT INTO users (nome, idade) VALUES (%s, %s)"

    cursor = my_db.cursor()
    cursor.execute(sql, values)

    my_db.commit()

    print(cursor.rowcount, "record inserted.")


def select(name):
    mydb = mysql.connector.connect(
        host="localhost",
        user="user",
        password="123456",
        database=name
        )

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users")
    myresult = cursor.fetchall()

    return [x for x in myresult]

###
if __name__ == '__main__':
    name_db = 'db_users'
    c = create_db(name=name_db)
    create_table(cursor=c, name=name_db)
    insert(name=name_db)
    select(name=name_db)


# print(check_dbases())