class Employee:
    """Describe Employee class"""

    def __init__(self, first_name, last_name, department, year):
        """Initialize Employee attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.dept = department

        if year > 2024:
            raise ValueError("Year cannot be greater than current year")

        self.year = year

    def __str__(self):
        """Return string representation of Employee"""
        return f"{self.first_name} {self.last_name}, {self.dept}, {self.year}"


def add_emp():
    """Add Employee to list"""
    employees = []
    while True:
        try:
            employee = (
                Employee(input("First name: "), input("Last name: "), input("Department: "), int(input("Year: "))))
        except Exception as e:
            print("Invalid input,", e)
            continue

        employees.append(employee)

        choice = input("Enter '1' for exit: ").strip()
        if choice == "1":
            break

    return employees


def find_emp(employees):
    """Find Employees"""
    founded = []
    for e in employees:
        if e.year > 2024 or e.year < 2000:
            founded.append(e)

    return founded


if __name__ == "__main__":
    employee_list = add_emp()
    founded_employees = find_emp(employee_list)

    print("\nEmployee whose data needs to be updated:")
    if len(founded_employees) == 0:
        print("\tThere are no such")
    else:
        for emp in founded_employees:
            print("\t", emp)
