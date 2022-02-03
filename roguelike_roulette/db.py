import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS games (id INTEGER PRIMARY KEY, game text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM games ORDER BY id asc")
        rows = self.cur.fetchall()
        return rows

    def insert(self, game):
        self.cur.execute("INSERT INTO games VALUES (NULL, ?)", (game,))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM games WHERE id=?", (id,))
        self.conn.commit()

    def clear_list(self):
        self.cur.execute("DELETE FROM games;")
        self.conn.commit()

    def __del__(self):
        self.conn.close()


#db.clear_list()