#! /usr/bin/python3
import sys

sys.version_info[0]

lab_exercise = "Generators"
lab_type = "lab-code"
python_version = ("%s.%s.%s" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))
print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))

#====================================

#CODE1: Create a Generator Function that implements and yields the Fibonacci sequence

#CODE2: Iterate over the fibonacci generator function

#CODE3: Use Generator Expressions to discover sum, min, and max of the square roots of a random list of numbers

#CODE4: Use f-string to format and print sum, min, and max