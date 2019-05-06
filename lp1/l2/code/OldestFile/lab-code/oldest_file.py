#! /usr/bin/python3
import sys
sys.version_info[0]

lab_exercise = "OldestFile"
lab_type = "lab-code"
python_version = ("%s.%s.%s" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))

print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))
print()

#====================================

#CODE1: Import os and datetime modules

#CODE2: Test input args to the script

#CODE3: get files in specified directory and prepend the full path

#CODE4: filter out non-files

#CODE5: transform list of filenames into list of (filename,unixtimestamp) tuples

#CODE6: sort files by timestamp

#CODE7: convert from Unix timestamp to python datetime object

#CODE8: print as human-readable date (which it defaults to)
