## Challenge 1-3-3
#write a program to read in a string of students and gpas in one input statement like this:

#`mike 3.4, noel 3.2, obby 3.5, peta 3.4`
#and write out JSON like this:

#```
#[
#    { "name" : "mike", "gpa" : 3.4 },
#    { "name" : "noel", "gpa" : 3.2 },
#    { "name" : "obby", "gpa" : 3.5 },
#    { "name" : "peta", "gpa" : 3.4 }
#]
#```

#Suggested approach:
#''''''
#    1. input text
#    2. for each student split on "," from the text
#    3.    split the student into name and gpa 
#    4.    parse the gpa so its a float
#    5.    add the name and gpa to the list
#    6. write the list to students.json as JSON
#''''''

import json
input_string = input("Enter students and GPAs (e.g., 'mike 3.4, noel 3.2'): ")
students_list = []
students = input_string.split(',')
for student in students:
    name, gpa = student.strip().split()
    students_list.append({"name": name, "gpa": float(gpa)})
with open('students.json', 'w') as json_file:
    json.dump(students_list, json_file)
