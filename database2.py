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

#INset records

curs.execute("INSERT INTO customers VALUES ('Mary', 'Brown','Mary.Brownn@me.com')")
print("Insert executed successfully")

#commit our command
conn.commit()

# Close connection
conn.close()