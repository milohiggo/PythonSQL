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

#Update records




curs.execute("""UPDATE customers SET first_name = 'MRS Mary'
                 WHERE first_name = 'Mary'

""")

#commit our command
conn.commit()

curs.execute("SELECT * FROM customers where last_name = 'Brown'")
#print (curs.fetchall())

items = curs.fetchall()

# print (items)
 
# Create loop
print("NAME" + "\t\tLAST NAME")
for item in items:
    print (item)

 
# Close connection
conn.close()