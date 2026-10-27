class Employee:
    def __init__(self, employee_id, name, role, salary):
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.salary = salary

    def display_details(self):
        print(f"{self.employee_id} - {self.name} - {self.role} - ₹{self.salary}")


FILE_NAME = "employees.txt"


def create_sample_file():
    sample_data = [
        "101,Rahul,Python Developer,50000",
        "102,Anjali,Tester,45000",
        "103,John,Developer,60000",
        "104,Priya,Tester,48000",
    ]
    with open(FILE_NAME, "w") as file:
        for line in sample_data:
            file.write(line + "\n")


def add_employee(employee):
    with open(FILE_NAME, "a") as file:
        file.write(f"{employee.employee_id},{employee.name},{employee.role},{employee.salary}\n")


def read_employees():
    employees = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                employee_id, name, role, salary = line.split(",")
                employees.append(Employee(employee_id, name, role, int(salary)))
    except FileNotFoundError:
        print(f"Error: {FILE_NAME} was not found.")
    return employees


def find_highest_salary(employees):
    if not employees:
        return None
    highest = employees[0]
    for emp in employees[1:]:
        if emp.salary > highest.salary:
            highest = emp
    return highest


def find_employees_by_role(employees):
    role_count = {}
    for emp in employees:
        role_count[emp.role] = role_count.get(emp.role, 0) + 1
    return role_count


def main():
    create_sample_file()
    employees = read_employees()

    print("===== Employee Details =====\n")
    for emp in employees:
        emp.display_details()

    print("\n===== Employees with Salary > 50000 =====\n")
    for emp in employees:
        if emp.salary > 50000:
            print(f"{emp.name} - ₹{emp.salary}")

    highest = find_highest_salary(employees)
    if highest:
        print("\nHighest Paid Employee:")
        print(f"{highest.name} - ₹{highest.salary}")

    print("\nEmployee Count by Role:")
    for role, count in find_employees_by_role(employees).items():
        print(f"{role}: {count}")


if __name__ == "__main__":
    main()