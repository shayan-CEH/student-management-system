import json
import os
import re

# File jahan students store honge
FILENAME = "students.json"

# ----------------- Load & Save Students -----------------
def load_students():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_students(students):
    with open(FILENAME, "w") as f:
        json.dump(students, f, indent=4)

# ----------------- Validation Functions -----------------
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def is_unique_roll(roll_no, students):
    for s in students:
        if s["roll_no"] == roll_no:
            return False
    return True

def get_non_empty_input(prompt):
    while True:
        value = input(prompt)
        if value.strip() != "":
            return value
        print("❌ Field cannot be empty!")

# ----------------- Add Student -----------------
def add_student():
    students = load_students()
    print("\n--- Add New Student ---")
    
    name = get_non_empty_input("Enter student name: ")
    
    while True:
        roll_no = get_non_empty_input("Enter roll number: ")
        if is_unique_roll(roll_no, students):
            break
        print("❌ Roll number already exists! Try another.")
    
    student_class = get_non_empty_input("Enter student class: ")
    
    while True:
        age = get_non_empty_input("Enter age: ")
        if age.isdigit() and 3 <= int(age) <= 100:
            break
        print("❌ Enter valid age (3-100).")
    
    gender = get_non_empty_input("Enter gender (Male/Female/Other): ")
    contact = get_non_empty_input("Enter contact number: ")
    
    while True:
        email = get_non_empty_input("Enter email: ")
        if is_valid_email(email):
            break
        print("❌ Invalid email format!")
    
    address = get_non_empty_input("Enter address: ")

    student = {
        "name": name,
        "roll_no": roll_no,
        "class": student_class,
        "age": age,
        "gender": gender,
        "contact": contact,
        "email": email,
        "address": address
    }
    students.append(student)
    save_students(students)
    print("✅ Student added successfully!\n")

# ----------------- View Students -----------------
def view_students():
    students = load_students()
    if not students:
        print("No students found.\n")
        return
    print("\n--- All Students ---")
    for i, s in enumerate(students, 1):
        print(f"{i}. Name: {s['name']}")
        print(f"   Roll No: {s['roll_no']}, Class: {s['class']}, Age: {s['age']}, Gender: {s['gender']}")
        print(f"   Contact: {s['contact']}, Email: {s['email']}, Address: {s['address']}")
        print("-" * 50)
    print()

# ----------------- Update Student -----------------
def update_student():
    students = load_students()
    roll_no = input("Enter roll number of student to update: ")
    for s in students:
        if s["roll_no"] == roll_no:
            print("\n--- Update Student Details ---")
            s["name"] = input(f"Enter new name ({s['name']}): ") or s['name']
            s["class"] = input(f"Enter new class ({s['class']}): ") or s['class']
            
            while True:
                age = input(f"Enter new age ({s['age']}): ") or s['age']
                if age.isdigit() and 3 <= int(age) <= 100:
                    s['age'] = age
                    break
                print("❌ Enter valid age (3-100).")
            
            s["gender"] = input(f"Enter new gender ({s['gender']}): ") or s['gender']
            s["contact"] = input(f"Enter new contact ({s['contact']}): ") or s['contact']
            
            while True:
                email = input(f"Enter new email ({s['email']}): ") or s['email']
                if is_valid_email(email):
                    s['email'] = email
                    break
                print("❌ Invalid email format!")
            
            s["address"] = input(f"Enter new address ({s['address']}): ") or s['address']
            save_students(students)
            print("✅ Student updated successfully!\n")
            return
    print("❌ Student not found!\n")

# ----------------- Delete Student -----------------
def delete_student():
    students = load_students()
    roll_no = input("Enter roll number of student to delete: ")
    for s in students:
        if s["roll_no"] == roll_no:
            students.remove(s)
            save_students(students)
            print("✅ Student deleted successfully!\n")
            return
    print("❌ Student not found!\n")

# ----------------- Search Student -----------------
def search_student():
    students = load_students()
    if not students:
        print("No students in database.\n")
        return
    print("\n--- Search Students ---")
    print("You can search by name, class, roll number, or email.")
    keyword = input("Enter search keyword: ").lower()
    found = False
    for s in students:
        if (keyword in s["name"].lower() or
            keyword in s["roll_no"].lower() or
            keyword in s["class"].lower() or
            keyword in s["email"].lower()):
            print(f"Name: {s['name']}, Roll No: {s['roll_no']}, Class: {s['class']}, Age: {s['age']}, Gender: {s['gender']}")
            print(f"Contact: {s['contact']}, Email: {s['email']}, Address: {s['address']}")
            print("-" * 50)
            found = True
    if not found:
        print("❌ No student found!\n")
    else:
        print()

# ----------------- Main Menu -----------------
def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("❌ Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()