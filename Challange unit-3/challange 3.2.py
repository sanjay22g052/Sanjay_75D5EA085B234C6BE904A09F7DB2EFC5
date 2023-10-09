class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

   
def sort_students(student_list):
    # Sort the student list in descending order based on CGPA
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of students
students = [
    Student("Hari", "A123", 7.9),
    Student("Srikanth", "A124", 8.9),
    Student("Saumya", "A125", 9.1),
    Student("Mahidhar", "A126", 9.9),
]

sorted_students = sort_students(students)

# Print the sorted students
for student in sorted_students:
    print("Name: {},Roll Number: {},CGPA: {}".format(student.name,student.roll_number,student.cgpa))

