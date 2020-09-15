from hr import calculate_payroll
import json
from productivity import track
from employees import Employee, employee_database


def print_dict(d):
    print(json.dumps(d, indent=2))


employees = employee_database.employees
track(employees, 40)
calculate_payroll(employees)

temp_secretary = Employee(5)
print("Temporary Secretary:")
print_dict(temp_secretary.to_dict())
