import cx_Oracle

class DB_Connection:
    ''' Make a connection with the database'''
    con = cx_Oracle.connect("SYSTEM/<yourPassword>$@localhost:1521/orcl")
    cur = con.cursor()