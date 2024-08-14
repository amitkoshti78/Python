import sys
import psycopg2
from psycopg2 import OperationalError, errorcodes, errors

def db_query(conn):
    
    try:
        if conn != None:

        # declare a cursor object from the connection
            cursor = conn.cursor()
            #print ("cursor object:", cursor, "\n")
    except psycopg2.OperationalError:
        print("Print cursor state invalid")
        cursor.close()
    else:
        print("Cusrsor opened")
        
    
    try:
        cursor.execute("SELECT * FROM Customer;")
    except psycopg2.OperationalError:
        print("SELECT statement failed")
    else:
        rows = cursor.fetchall()
        print(rows)
    finally:
        print("Cursor closed")
        cursor.close()
        


    
    
def db_connect():
    try:
        conn = psycopg2.connect(database = "postgres", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "Admin",
                        port = 5432)
    except psycopg2.DatabaseError:
        print("Data base connection error")
        conn = None
    except psycopg2.OperationalError:
        print("Data base connection error")
        conn = None
    else:
        print("Database connected successfully")
        db_query(conn)
    finally:
        print("Data base closed")
        conn.close()
        
def main():
    db_connect()

if __name__ == '__main__' :
    main()
        