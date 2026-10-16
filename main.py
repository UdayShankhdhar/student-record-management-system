import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("students.json")


def load_students():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read the data file. Starting with an empty record list.")
        return []


def save_students(students):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    name = input("Student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        roll_no = int(input("Roll number: "))
        marks = float(input("Marks (0-100): "))
    except ValueError:
        print("Roll number must be an integer and marks must be a number.")
        return

    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
        return
    if any(student["roll_no"] == roll_no for student in students):
        print("That roll number already exists.")
        return

    students.append({"roll_no": roll_no, "name": name, "marks": marks})
    save_students(students)
    print("Student added successfully.")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n{:<12} {:<25} {:>8}".format("Roll No.", "Name", "Marks"))
    print("-" * 47)
    for student in students:
        print("{:<12} {:<25} {:>8.2f}".format(
            student["roll_no"], student["name"], student["marks"]
        ))


def search_student(students):
    try:
        roll_no = int(input("Enter roll number to search: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    for student in students:
        if student["roll_no"] == roll_no:
            print(
                f'Found: {student["name"]} | '
                f'Roll No: {student["roll_no"]} | Marks: {student["marks"]:.2f}'
            )
            return
    print("Student not found.")


def delete_student(students):
    try:
        roll_no = int(input("Enter roll number to delete: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    for index, student in enumerate(students):
        if student["roll_no"] == roll_no:
            removed = students.pop(index)
            save_students(students)
            print(f'Removed record for {removed["name"]}.')
            return
    print("Student not found.")


def main():
    students = load_students()
    actions = {
        "1": add_student,
        "2": view_students,
        "3": search_student,
        "4": delete_student,
    }

    while True:
        print("\n=== Student Record Management System ===")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student by roll number")
        print("4. Delete student")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action(students)
        else:
            print("Invalid option. Please choose from 1 to 5.")


if __name__ == "__main__":
    main()
