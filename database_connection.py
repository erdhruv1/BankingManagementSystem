import cx_Oracle

class DB_Connection:
    ''' Make a connection with the database'''
    con = cx_Oracle.connect("SYSTEM/oracle@localhost:1521/orclcdb")
    cur = con.cursor()