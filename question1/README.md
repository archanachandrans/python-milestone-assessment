# Student Marks Management System

A simple Python console program that records marks for several students, calculates each student's total, average, grade, and result, and prints a summary with the highest-scoring student and the students who averaged above 75.

## Features

- Collects student ID, name, and marks in Python, SQL, and AI
- Calculates the total and average (rounded to 2 decimal places)
- Assigns a grade: A (80+), B (60–79.99), C (40–59.99), F (below 40)
- Shows PASS if the average is 40 or more, otherwise FAIL
- Finds the student with the highest average
- Lists the students whose average is above 75

## Requirements

- Python 3.8 or later (no external libraries are needed)

## How to Run

1. Open a terminal in the project folder.
2. Run the program:

   ```bash
   python main.py
   ```

3. Enter the number of students, then enter each student's details when prompted.

## Example

```
Enter number of students: 2
Enter Student ID: 001
Enter Student Name: Rahul
Enter the mark for Python: 90
Enter the mark for SQL: 70
Enter the mark for AI: 80
Enter Student ID: 002
Enter Student Name: Raj
Enter the mark for Python: 89
Enter the mark for SQL: 79
Enter the mark for AI: 80

===== Student Result =====

Student ID: 001
Name: Rahul
Total: 240
Average: 80.0
Grade: A
Result: PASS

Student ID: 002
Name: Raj
Total: 248
Average: 82.67
Grade: A
Result: PASS

Highest Scoring Student: Raj
Students above 75: Rahul, Raj
```

## Grading Rules

| Average        | Grade | Result |
|----------------|-------|--------|
| 80 or more     | A     | PASS   |
| 60 to below 80 | B     | PASS   |
| 40 to below 60 | C     | PASS   |
| Below 40       | F     | FAIL   |

## Project Structure

```
main.py   # All program code
README.md          # This file
```

## Code Overview

| Function | Purpose |
|----------|---------|
| `student_details()` | Asks for each student's data and returns a list of student records |
| `student_grade(average)` | Returns the grade letter for an average |
| `student_result(average)` | Returns PASS or FAIL for an average |
| `student_highest(students)` | Returns the student with the highest average |

## Limitations

- Input is not validated. A non-numeric mark stops the program with an error.
- Marks are not range-checked, so values outside 0–100 are accepted.
- Results are shown only in the terminal and are not saved to a file.