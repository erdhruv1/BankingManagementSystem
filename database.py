from database_connection import DB_Connection

class Database:

    def __init__(self):
        self.connection = DB_Connection.con
        self.cursor     = DB_Connection.cur

    def make_tables(self):
        sql = "select count(*) from user_tables where table_name = 'CUSTOMERS'"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()

        #If table name with CUSTOMERS already exist then simply return back
        if res[0][0] != 0:
            return

        #If table name with CUSTOMERS not exist then start creating tables
        sql = """create table customers(
                          customer_id number(5) primary key,
                          first_name varchar2(10),
                          last_name varchar2(10),
                          status varchar2(10),
                          city varchar2(10),
                          password varchar2(20))"""
        self.cursor.execute(sql)

        sql = """create sequence customer_id_sequence
                    start with 1
                    increment by 1
                    nocycle"""
        self.cursor.execute(sql)

        self.connection.commit()

    def sign_up_customer(self, customer):
        fname = customer.get_first_name()
        lname = customer.get_last_name()
        password = customer.get_password()
        city = customer.get_city()
        sql = "select customer_id_sequence.nextval from dual"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        id = res[0][0]
        status = customer.get_status()
        sql = "insert into customers values(:id, :fname, :lname,:status, :city, :password)"
        self.cursor.execute(sql, {"id": id, "fname": fname, "lname": lname, "password": password, "status": status, "city": city})
        self.connection.commit()
        print("Congratulations ! Your Account was Created Successfully")
        print("Your Customer ID : ", id)