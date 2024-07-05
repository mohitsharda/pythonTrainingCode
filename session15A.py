# DATABASE OOPS

import mysql.connector as db

class Database:

    def __init__(self):
        self.connection = db.connect(user = "root",
                        password = "656434",
                        host = "127.0.0.1",
                        database = "project",
                    )
        print("[DATABASE] CONNECTION CREATED: ")

        self.cursor = self.connection.cursor()
        print("[DATABASE] Cursor Created: ")

    # Insert/update or delete in DB
    def write(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()
        print("[DATABASE] SQL STATEMENT EXECUTED SUCCESSFULLY: ")

    # fetch data from DB
    def read(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result


