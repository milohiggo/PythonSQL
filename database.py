# -*- coding: utf-8 -*-
"""
Video https://www.youtube.com/watch?v=byHcYRpMgI4
Created on Sat May 29 20:17:56 2021

@author: ssaghi
"""
import sqlite3
# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')

#Create cursor
curs = conn.cursor()

#Create table
# Data Types: NULL (boolean), INTEGER (just numbers), REAL(decimals), TEXT, BLOB 

curs.execute("""CREATE TABLE customers (
    first_name DATATYPE text,
    last_name  DATATYPE text,
    email DATATYPE text
)""")

#example in single line
#curs.execute("CREATE TABLE customers (first_name DATATYPE,last_name  DATATYPE, email DATATYPE)")

#commit our command
conn.commit()

# Close connection
conn.close()