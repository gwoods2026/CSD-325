import json
filename = 'student.json'

#This displays the list and sets it up to display how we need it
def print_student_info(student_data):
    for student in student_data:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

#loads file
with open(filename, 'r') as f:
    students = json.load(f)

print("\n--- Original Student list ---")

#calls function
print_student_info(students)

#add new student to list
new_student = {"L_Name": "Woods", "F_Name": "Garrett", "Student_ID": 40165, "Email": "gwoods@gmail.com"}
students.append(new_student)

print("\n--- New Student list ---")
print_student_info(students)

# updates file with new student
with open(filename, 'w') as f:
    json.dump(students, f, indent=4)
    print("\nFile updated with new student information")
