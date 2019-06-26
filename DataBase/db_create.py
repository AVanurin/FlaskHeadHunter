import sqlite3

PATH_TO_BD = "MyDB.db"

def init():
    conn = sqlite3.connect(PATH_TO_BD)
    c = conn.cursor()

    q = '''
    CREATE TABLE Users
    (
    id INT,
    name VARCHAR(50),
    city VARCHAR(50)
    );
    '''

    c.execute(q)
    conn.commit()
    conn.close()

def add_user(_id, name, city):
    conn = sqlite3.connect(PATH_TO_BD)
    c = conn.cursor()

    q = f'''
    INSERT INTO clients VALUES
    (
    {_id},
    "{name}",
    "{city}"
    );
    '''

    c.execute(q)
    conn.commit()
    conn.close()
