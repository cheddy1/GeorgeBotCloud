import atexit
import sqlite3
import json

con = sqlite3.connect("app/db.db", check_same_thread=False)
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS frames (stamp float PRIMARY KEY)")


def temp_store():
    with open('app/lidar_frame.json', 'r') as f:
        cur.execute("DELETE FROM frames")
        data = f.read()
        json_data = json.loads(data)
        stamps = list()
        for c, frame in enumerate(json_data):
            stamps.append(float(frame["header"]["stamp"]))
        cur.executemany(f"INSERT OR IGNORE INTO frames (stamp) VALUES (?)", zip(stamps))
        con.commit()


def execute_sql(sql, s_type):
    res = cur.execute(sql)
    if s_type == 'insert':
        con.commit()
    else:
        return res


atexit.register(con.close)
