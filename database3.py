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

#Insert many records
many_customers = [('M1', 'Brown','M1.Brownn@me.com'),
                  ('M2', 'Brown','M2.Brownn@me.com'),
                  ('M3', 'Brown','M3.Brownn@me.com')]

curs.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)
print("Insert many executed successfully")

#commit our command
conn.commit()

# Close connection
conn.close()