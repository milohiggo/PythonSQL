# -*- coding: utf-8 -*-
"""
Video https://www.youtube.com/watch?v=byHcYRpMgI4
Created on Sat May 29 20:17:56 2021

@author: ssaghi
"""
import sqlite3


# Query the Database
def show_all():
   # conn = sqlite3.connect(':memory:')
    conn = sqlite3.connect('customer.db')
    #Create cursor
    curs = conn.cursor()
    # Query DB
    curs.execute("SELECT rowid, * FROM customers")
    #print (curs.fetchall())
    items = curs.fetchall()
    # print (items)
    # Create loop
    print("ROWID"+ "  " + "NAME" + "\t\tLAST NAME")
    for item in items:
        print (str(item[0]) + " "+ item[1] + "\t\t " + item[2])
    #commit our command
    conn.commit()
    # Close connection
    conn.close()

def add_one(first,last,email):
    # conn = sqlite3.connect(':memory:')
    conn = sqlite3.connect('customer.db')
    #Create cursor
    curs = conn.cursor()
    curs.execute("INSERT INTO customers VALUES (?,?,?)",(first,last,email))
    print("Insert executed successfully")
     #commit our command
    conn.commit()
    # Close connection
    conn.close()

def query_one(id):
    # conn = sqlite3.connect(':memory:')
    conn = sqlite3.connect('customer.db')
    #Create cursor
    curs = conn.cursor()
    curs.execute("select * FROM customers WHERE rowid =(?)",id)
    items = curs.fetchall()
    print (items)
    conn.commit()
    # Close connection
    conn.close()
