print("Welcome to my Application!")


nameOfStudents = input("Enter your name: ")

def welcome(nameOfStudents):
    print("Hello,", nameOfStudents, "!")

students = ["Azzam", "Yaseen", "Huzaifa"]
if nameOfStudents in students:
    print("Welcome back, ", nameOfStudents, "!")
else:
    print("Welcome, ", nameOfStudents, "!")
print("List of students:")
for student in students:
    print(student)

while True:
    admission = input("Do you want to add a new student? (yes/no): ")
    if admission.lower() == "yes":
        new_student = input("Enter the name of the new student: ")
        students.append(new_student)
    else:
        break

print("Updated list of students:")
for student in students:
    print(student)

print("Goodbye! Thanks for using the application.")
