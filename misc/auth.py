from misc import loading, tools, prints, request, update
import sqlite3

con = sqlite3.connect("auth.db")
cur = con.cursor()

def create():
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                user TEXT,
                passwd TEXT
    )""")

def newUser(user, password):
    cur.execute("SELECT * FROM users WHERE user=?", (user,))

    if cur.fetchone():
        print("Usuário já existe.")
        return None
    
    cur.execute(f"""INSERT INTO users (user, passwd) VALUES (?, ?)""", (user, password))

    con.commit()


def check(user, password):
    cur.execute("SELECT * FROM users WHERE user=?", (user,))
    usuario = cur.fetchone()

    if usuario and usuario[2] == password:
        if usuario[1] == "yyax":
            return "ADM"
        else:
            return "Yes"
    else:
        return "No"

    

def delete(user):
    cur.execute("SELECT * FROM users WHERE user=?", (user,))

    if not cur.fetchone():
        print("Usuário não existe.")
        return
    
    if input(f"Deseja realmente deletar {user} (s/n)? ") in ['s', 'S', 'y', 'Y']:
        cur.execute("DELETE FROM users WHERE user=?", (user,))
        con.commit()
    else:
        pass