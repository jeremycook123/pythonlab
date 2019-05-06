#! /usr/bin/python3
import sys
sys.version_info[0]

lab_exercise = "SQLite3"
lab_type = "solution-code"
python_version = ("%s.%s.%s" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))

print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))
print()

#====================================

#CODE1: Import random, datetime, and sqlite modules
from random import choice
from datetime import date
import sqlite3

#CODE2: Create candidate info1 data
candidate_info1 = (46, 'Nader', 'Ralph', date(2017,1,20), date(2021,1,19), 'Winstead', 'Connecticut', date(1934,2,27), None, 'Independent')

#CODE3: Create candidate info2 data
candidate_info2 = (52, 'John', 'Doe', date(2017,1,20), date(2021,1,19), 'San Francisco', 'California', date(1970,7,16), None, 'Independent')

#CODE4: Connect to SQL database and insert records
with sqlite3.connect("./presidents.db") as conn:
   c = conn.cursor()

   insert_stmt = "INSERT INTO presidents (termnum, lastname, firstname, termstart, termend, birthplace, birthstate, birthdate, deathdate, party) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"

   try:
      rows1 = c.execute(insert_stmt, candidate_info1)
      rows2 = c.execute(insert_stmt, candidate_info2)
   except Exception as e:
      print("Error inserting record:", e)
      conn.rollback()
   else:
      print("Record inserted OK.")
      conn.commit()