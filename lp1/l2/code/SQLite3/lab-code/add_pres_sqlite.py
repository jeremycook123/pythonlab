#! /usr/bin/python3
import sys
sys.version_info[0]

lab_exercise = "SQLite3"
lab_type = "lab-code"
python_version = ("%s.%s.%s" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))

print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))
print()

#====================================

#CODE1: Import random, datetime, and sqlite modules

#CODE2: Create candidate info1 data

#CODE3: Create candidate info2 data

#CODE4: Connect to SQL database and insert records
with sqlite3.connect("../DATA/presidents.db") as conn:
    c = conn.cursor()

    insert_stmt = '''
       INSERT INTO presidents
    (termnum, lastname, firstname, termstart, termend,
     birthplace, birthstate, birthdate, deathdate, party)
         VALUES
        (?, ?, ?, ?, ?,
         ?, ?, ?, ?, ?);
    '''

    try:
        rows1 = c.execute(insert_stmt, candidate_info1)
        rows2 = c.execute(insert_stmt, candidate_info2)
    except Exception as e:
        print("Error inserting record:", e)
        conn.rollback()
    else:
        print("Record inserted OK.")
        conn.commit()
