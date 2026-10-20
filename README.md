# Digital Exam & Results Management System

A Python program that uses Object-Oriented Programming to record students and their exam results, then calculate averages and grades.

**Domain:** Education
**Course:** Department of Information and Communication Technology, Limkokwing University of Creative Technology, Sierra Leone

## Features
- Add students and record subject results
- Automatically calculates each student's average and grade (A-F)
- Update a student's record and display all records
- Simple menu-driven interface

## How to Run
```
python student_results_system.py
```
Requires Python 3.8 or later. No external libraries needed.

## Assignment Mapping

| Task | Where it is in the code |
|------|--------------------------|
| Task 1: Two classes with attributes, methods, object interaction | `Student` and `Result` classes. `Student.add_result()` stores `Result` objects |
| Task 2: One data structure | A dictionary `students` keyed by student ID, with `add_student()` and `display_students()` functions |
| Task 3: Instance and class methods | Instance: `add_result()`, `average()`, `grade()`, `display_info()`, `update_record()`. Class: `from_string()`, `get_total_students()` |

## Example Output
```
ID: S001 | Name: Aminata Kamara
  - Maths: 85
  - English: 78
  - Science: 90
  Average: 84.3 | Grade: A

ID: S002 | Name: Mohamed Sesay
  - Maths: 62
  - English: 70
  - Science: 55
  Average: 62.3 | Grade: C

Total students: 3
```

## Digital Public Goods (DPG) Alignment
- **Open source:** The code is published openly on GitHub for anyone to use, study and improve.
- **Inclusive and accessible design:** Plain text menus with clear prompts and error messages. It works on any computer with Python and needs no internet or special hardware.
- **Privacy-respecting:** Only a student ID, a name and scores are stored. No addresses, phone numbers, photos or other sensitive data are collected, and nothing is sent over a network.
- **Modular and reusable:** `Student` and `Result` are independent classes that can be reused in other systems (for example a school website or app).

## Author
Mohamed Swaray - 905005882
