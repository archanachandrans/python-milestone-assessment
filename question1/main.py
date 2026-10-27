# student = [{ "Student ID" : 101, "Name": "Rahul", "Python": 75, "SQL": 81, "AI": 84 },
#            { "Student ID" : 102, "Name": "Anjali", "Python": 78, "SQL": 88, "AI": 90},
#            { "Student ID" : 103, "Name": "John", "Python": 76, "SQL": 44, "AI": 89},
#            { "Student ID" : 104, "Name": "Radhu", "Python": 60, "SQL": 34, "AI": 50}]

# for s in student:
#     total = s["Python"] + s["SQL"] +s["AI"]
#     print(f"{s['Name']}: {total}")
# class Students:  
#     def get_student_details():
#         name = input("Enter the student name: ")    #Ask user for an input
#         student = {"Name" : name}                   #Use the value from user to the key in a dictionary
#         id = input("Enter the student id: ")
#         student = {"Student id" : id}
#         subjects = ["Python", "SQL", "AI"]

#         for subject in subjects:
#             score = int(input(f"Enter the score of {subject}: ")) #Here int is used becoz input() returns a string value
#             student[subject]= score
#             #print(f"{subject} : {score} ")
#         for key in student:
#             print(f"{key}: {student[key]}")

#         return student
# student_count = int(input("Enter the number of students: "))
# for i in range(student_count):
#     result = Students()

#print(result)

def student_details():
    num_students    = int(input("Enter number of students: "))
    students        =[]
    for i in range (num_students):
        student_id      = input("Enter Student ID: ")
        name            = input("Enter Student Name: ")
        student = {
            "ID": student_id,
            "name": name,
            "Python": int(input("Enter the mark for Python: ")),
            "SQL": int(input("Enter the mark for SQL: ")),
            "AI": int(input("Enter the mark for AI: ")),
        }
        total               = student["Python"] + student["SQL"] + student["AI"]
        average             = round(total/3, 2)
        student["Total"]    = total
        student["Average"]  = average
        student["Grade"]    = student_grade(average)
        student["Result"]   = student_result(average)
        students.append(student)
    return students
def student_grade(average):
    if average >= 80:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "F"
def student_result(average):
    if average >= 40:
        return "PASS"
    else:
        return "FAIL"

def student_highest(students):
    best = students[0]
    for s in students[1:]:
        if s["Average"] > best["Average"]:
            best = s
    return best
students = student_details()
print("===== Student Result =====")
for s in students:
    print(f"\nStudent ID: {s['ID']}")
    print(f"Name: {s['name']}")
    print(f"Total: {s['Total']}")
    print(f"Average: {s['Average']}")
    print(f"Grade: {s['Grade']}")
    print(f"Result: {s['Result']}")
best = student_highest(students)
above_75 = [s["name"] for s in students if s["Average"] >75]
print(f"\nHighest Scoring Student: {best['name']}")
print(f"Students above 75: {', '.join(above_75) if above_75 else 'None'}")