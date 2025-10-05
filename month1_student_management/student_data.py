students = []

def add_student():
    """
    TODO: Prompt the user to enter student name, age, and grade.
    

    Append the student as a dictionary to the students list.
    """
    pass 

    student_name = input("Enter your name: ").strip()
    while student_name == "":
        print("Name cannot be empty. Please enter a valid name.")
        student_name = input("Enter your name: ").strip()

    # collecting student age and ensuring it's a positive integer.
    student_age = int(input("Enter your age: "))

    while student_age <= 0:
        print("Age must be a positive integer. Please enter a valid age.")
        student_age = int(input("Enter your age: ")).strip()

    # collecting student grade and ensuring it's a float between 0 and 100.
    student_grade = float(input("Enter your grade: "))

    while student_grade < 0 or student_grade > 100:
        print("Grade must be between 0 and 100. Please enter a valid grade.")
        student_grade = float(input("Enter your grade: "))

    # creating a dictionary to store student information
    student = {
        "name": student_name,
        "age": student_age,
        "grade": student_grade
    }
    students.append(student)
    
    print(f"Student Name: {student_name}, Age: {student_age}, Grade: {student_grade} added successfuly!\n")
add_student()


def view_students():
    """
     TODO: Loop through the students list and print each student's info.
    """
    pass

    if not students:
        print("No student data available.\n")
        return
    print ("Student Data:")

    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
        print()  # for better readability
view_students()


def get_average_grade():
    """
    TODO: Return the average grade of all students.
    """
    pass

    if not students:
        print("No student data available to calculate average grade.\n")
        return
    for student in students:
        total_grade = 0
        total_grade += student['grade']

        average = total_grade / len(students)
        print(f"Average Grade: {average:.3f}\n")
        return average