import mysql.connector as c
try:
    conn=c.connect(host="localhost",user="root",passwd="developer",database="school")
    if conn.is_connected():
        print("successfully connected")
except FileExistsError:
    print("SOMETHING WRONG")
