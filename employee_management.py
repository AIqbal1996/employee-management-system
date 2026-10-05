# Employee Management System


# Employee Class
class Employee:

    # Constructor
    def __init__(self, employee_id, name, department, salary, designation):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary
        self.designation = designation

    # Display employee information
    def display_info(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print("Designation:", self.designation)
        print("------------------------")

    # Update salary
    def update_salary(self, new_salary):
        self.salary = new_salary
        print(self.name, "salary updated to", self.salary)

    # Calculate annual salary
    def annual_salary(self):
        return self.salary * 12


# Create 5 Employee Objects

employee1 = Employee(
    101,
    "Arif",
    "Data Science",
    50000,
    "Senior Technical Lead"
)

employee2 = Employee(
    102,
    "Rahul",
    "IT",
    45000,
    "Software Engineer"
)

employee3 = Employee(
    103,
    "Amit",
    "HR",
    40000,
    "HR Manager"
)

employee4 = Employee(
    104,
    "Priya",
    "Finance",
    55000,
    "Finance Manager"
)

employee5 = Employee(
    105,
    "Neha",
    "Marketing",
    35000,
    "Marketing Executive"
)


# Display Employee Information

employee1.display_info()
employee2.display_info()
employee3.display_info()
employee4.display_info()
employee5.display_info()


# Update Salary

employee1.update_salary(60000)


# Calculate Annual Salary

print("Arif Annual Salary:", employee1.annual_salary())