# 1. Initialize an Empty Dictionary
# Create an empty dictionary named student_grades.
student_grades = {}


# 2. Add Students and Grades to the Dictionary
# Write a function add_student(name, grade) that adds a student and their grade to the dictionary and prints a message indicating the student was added.
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Student '{name}' was added with the grade of {grade}")


# 3. Remove Students from the Dictionary
# Write a function remove_student(name) that removes a student from the dictionary if they exist, and prints a message indicating the student was removed or a message if the student was not found.
def remove_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"Student '{name}' was removed.")
    else:
        print(f"Student {name} not found.")


# 4. Display All Students and Their Grades
# Write a function display_students() that prints all the students and their grades.
def display_students():
    print("Students:")
    for name, grade in student_grades.items():
        print(f"{name}: {grade}")


# 5. Update a Student's Grade
# Write a function update_grade(name, grade) that updates the grade of a student if they exist, and prints a message indicating the grade was updated or a message if the student was not found.
def update_grade(name, grade):
    student_grades.update({name: grade})
    if name in student_grades:
        print(f"Student '{name}' grade has been updated to {grade}")
    else:
        print(f"Student '{name}' not found")


# Add students
add_student("Dakota", 95)
add_student("Maggie", 96)
add_student("Cory", 100)
add_student("Raine", 65)
print()

# Display all students
display_students()
print()

# Remove student
remove_student("Raine")
print()

# Display all students
display_students()
print()

# Update student grade
update_grade("Dakota", 98)
print()

# Display all students
display_students()
