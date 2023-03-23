import sqlite3

con = sqlite3.connect("app/db.db")
cur = con.cursor()


def db_init():
    print("woo")
    # cur.execute("CREATE TABLE IF NOT EXISTS frames (column_name datatype, column_name datatype)")
