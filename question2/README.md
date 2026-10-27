# Simple Employee File Management

A Python console program that stores employee records in a text file, reads them back, and prints a report with employee details, high earners, the highest-paid employee, and a count of employees per role.

## Features

- Creates `employees.txt` with sample employee data
- Reads employee records from the file into `Employee` objects
- Displays all employees
- Lists employees with a salary above ₹50,000
- Finds the highest-paid employee
- Counts employees for each role
- Handles a missing file without crashing

## Requirements

- Python 3.8 or later (no external libraries needed)

## How to Run

1. Open a terminal in the project folder.
2. Run:

   ```bash
   python main.py
   ```

The program creates `employees.txt` automatically each time it runs, so you don't need to create it by hand.

## Example Output

```
===== Employee Details =====

101 - Rahul - Python Developer - ₹50000
102 - Anjali - Tester - ₹45000
103 - John - Developer - ₹60000
104 - Priya - Tester - ₹48000

===== Employees with Salary > 50000 =====

John - ₹60000

Highest Paid Employee:
John - ₹60000

Employee Count by Role:
Developer: 1
Python Developer: 1
Tester: 2
```

## File Format

Each line in `employees.txt` holds one employee, with fields separated by commas:

```
ID,Name,Role,Salary
101,Rahul,Python Developer,50000
```

## Code Overview

| Item | Purpose |
|------|---------|
| `Employee` class | Holds one employee's data and displays it |
| `create_sample_file()` | Writes the sample records to `employees.txt` |
| `add_employee(employee)` | Appends a new employee to the file |
| `read_employees()` | Reads the file and returns a list of `Employee` objects |
| `find_highest_salary(employees)` | Returns the employee with the highest salary |
| `find_employees_by_role(employees)` | Returns a dictionary of role counts |
| `main()` | Runs the program in order |

## Limitations

- The file is rewritten with sample data on every run, so any employees you add with `add_employee()` are lost on the next run.
- Records are assumed to have exactly four comma-separated fields. A malformed line stops the read.
- Salary is not validated beyond being a whole number.
- The salary threshold (50,000) and the file name are fixed in the code.