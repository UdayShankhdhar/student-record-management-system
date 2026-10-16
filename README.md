# Student Record Management System

A beginner-friendly command-line project built with Python. It lets you manage student records and saves them in a local JSON file, so records remain available when you run the program again.

## Features

- Add a student with a roll number, name, and marks
- View all saved student records
- Search for a student by roll number
- Delete a student record
- Validate user input and prevent duplicate roll numbers
- Save records in `students.json`

## Requirements

- Python 3.8 or newer
- No third-party packages required

## How to run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python main.py
   ```

   On some systems, use `python3 main.py` instead.

## Project files

- `main.py` — application logic and menu
- `students.json` — local data storage; starts empty and is updated by the program
- `README.md` — project documentation

## Example

```text
=== Student Record Management System ===
1. Add student
2. View all students
3. Search student by roll number
4. Delete student
5. Exit
Choose an option (1-5): 1
Student name: Asha
Roll number: 101
Marks (0-100): 87
Student added successfully.
```

## Python concepts used

- Functions and modules
- Lists and dictionaries
- Loops and conditional statements
- Input validation and exception handling
- Reading and writing JSON files
- CRUD operations: create, read, and delete records (update can be added as an extension)

## Possible improvements

- Add an update-student feature
- Calculate grades or average marks
- Add unit tests
- Replace JSON storage with SQLite

## Note

This is a learning project. It stores data locally and does not include user authentication.
