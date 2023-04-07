import psycopg2
from datetime import datetime as dt
import time

#Change to fit UCI Rocket's names
hostname = 'localhost'
database = 'development'
username = 'postgres'
pwd = 'postgres'
port_id = 5432

conn = None
cur = None

try:# to not crash program
    #how the code connects to the database, how it opens database connection, allows to perform database transactions
    #check out what the with clause does
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id)

    tc_all = [(1.1), (1.2), (1.3),(1.4)]
    tc1 = tc_all[0]
    tc2 = tc_all[1]
    tc3 = tc_all[2]
    tc4 = tc_all[3]

    pt1 = 0.0
    pt2 = 25.0
    pt3 = 50.0
    pt4 = 75.0

    cur = conn.cursor() #opens a cursor, stores values from sql operations

    insert_script = 'INSERT INTO tc (tc1, tc2, tc3, tc4) VALUES (%s, %s, %s, %s)' #insert command,%s are placeholders
    insert_script_pt = 'INSERT INTO pt (pt1, pt2, pt3, pt4) VALUES (%s, %s, %s, %s)' #insert command,%s are placeholders

    for i in range(100):
        time.sleep(1)
        tc1 = tc1 + 1
        tc2 = tc2 + 10
        tc3 = tc3 + 0.1
        tc4 = tc4 + 0.01
        insert_values = (tc1, tc2, tc3, tc4)
        cur.execute(insert_script, insert_values)

        pt1 = (pt1 + 5)%100
        pt2 = (pt2 + 5)%100
        pt3 = (pt3 + 5)%100
        pt4 = (pt4 + 5)%100
        insert_values = (pt1, pt2, pt3, pt4)
        cur.execute(insert_script_pt, insert_values)
        conn.commit()#save transactions into database

except Exception as error:
    print(error)
finally:
    #need to close connection before closing python program
    #If statements allow for the close of database and cursor if connection works
    if cur is not None:
        cur.close() # needs to be closed after program is over
    if conn is not None:
        conn.close() #closes database
