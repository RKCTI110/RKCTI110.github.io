# KeeferR

# 11/17/2024

# P3HW2

# Employee Salary

# Get employee name from user input
employee_name = input("Enter employee's name: ")

# Define other variables
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
overtime_hours = max(0, hours_worked - 40)

# Calculate overtime hours
regular_hours = hours_worked - overtime_hours

# Calculate pay details
overtime_pay = overtime_hours * pay_rate * 1.5
regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

# Printing employee pay details
print("--- Employee Pay Details ---")
print(f"{'Employee Name:':<20}{employee_name:<15}")
print(f"{'Hours Worked:':<20} {'Pay Rate:':<15} {'Overtime:':<15} {'Overtime Pay:':<15} {'Regular Pay:':<15} {'Gross Pay:':<10}")
print("-------------------------------------------------------------------------")
print(f"{hours_worked:<20.2f} ${pay_rate:<15.2f} {overtime_hours:<15.2f} ${overtime_pay:<15.2f} ${regular_pay:<15.2f} ${gross_pay:<20.2f}")


# Run the function

