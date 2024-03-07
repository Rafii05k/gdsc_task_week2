# Step 1: Initialize an empty dictionary to store student information.
students_db = {}

# Step 2: Function to add a new student to the database.
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    
    # Create a dictionary to store the student's details.
    student_info = {'Name': name, 'Age': age, 'Grade': grade}
    
    # Add the student to the database with their name as the key.
    students_db[name] = student_info
    print(f"{name} has been added to the database.")

# Step 3: Function to view the details of a specific student.
def view_student():
    name = input("Enter student name to view details: ")
    
    # Check if the student exists in the database.
    if name in students_db:
        student_info = students_db[name]
        print(f"Student Details for {name}:\nAge: {student_info['Age']}\nGrade: {student_info['Grade']}")
    else:
        print(f"Student with name {name} not found in the database.")

# Step 4: Function to list all students in the database.
def list_all_students():
    print("List of all students in the database:")
    for name, student_info in students_db.items():
        print(f"{name}: Age - {student_info['Age']}, Grade - {student_info['Grade']}")

# Step 5: Function to update student information.
def update_student():
    name = input("Enter student name to update details: ")
    
    # Check if the student exists in the database.
    if name in students_db:
        student_info = students_db[name]
        print(f"Current Details for {name}:\nAge: {student_info['Age']}\nGrade: {student_info['Grade']}")
        
        # Collect updated information from the user.
        age = int(input("Enter new age: "))
        grade = input("Enter new grade: ")
        
        # Update the student's information in the database.
        students_db[name]['Age'] = age
        students_db[name]['Grade'] = grade
        
        print(f"Updated details for {name}:\nAge: {age}\nGrade: {grade}")
    else:
        print(f"Student with name {name} not found in the database.")

# Step 6: Function to delete a student from the database.
def delete_student():
    name = input("Enter student name to delete from the database: ")
    
    # Check if the student exists in the database.
    if name in students_db:
        del students_db[name]
        print(f"{name} has been deleted from the database.")
    else:
        print(f"Student with name {name} not found in the database.")

# Step 7: Main program loop to interact with the user.
while True:
    print("\nStudent Database Program Menu:")
    print("1. Add Student\n2. View Student\n3. List All Students\n4. Update Student Information\n5. Delete Student\n6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        view_student()
    elif choice == '3':
        list_all_students()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
