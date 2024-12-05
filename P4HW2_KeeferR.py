# KeeferR

# 12/5/2024

# P4HW2

# Employee Salary update multiple people and termination

'''
ALGORITHM PayrollCalculator
    Initialize total_overtime = 0
    Initialize total_regular = 0  
    Initialize total_gross = 0
    Initialize employee_count = 0
    
    Display welcome message
    
    WHILE TRUE
        Get employee_name from user
        IF employee_name in ['done', 'DONE', 'Done'] THEN
            BREAK
        END IF
        
        Increment employee_count
        Get hours_worked from user
        Get pay_rate from user
        
        Calculate overtime_hours = max(0, hours_worked - 40)
        Calculate regular_hours = hours_worked - overtime_hours
        Calculate overtime_pay = overtime_hours * pay_rate * 1.5
        Calculate regular_pay = regular_hours * pay_rate
        Calculate gross_pay = regular_pay + overtime_pay
        
        Add overtime_pay to total_overtime
        Add regular_pay to total_regular
        Add gross_pay to total_gross
        
        Display employee pay details
    END WHILE
    
    Display final summary with:
        - Total employees
        - Total regular pay
        - Total overtime pay
        - Total gross pay
END ALGORITHM
'''

# Initialize totals
total_overtime = 0
total_regular = 0
total_gross = 0
employee_count = 0

print("\n=== Employee Payroll System ===\n")

while True:
    employee_name = input("\nEnter employee's name or 'Done' to terminate: ")
    if employee_name in ['done', 'DONE', 'Done']:
        break
        
    employee_count += 1
    hours_worked = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))
    
    overtime_hours = max(0, hours_worked - 40)
    regular_hours = hours_worked - overtime_hours
    
    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay
    
    # Update totals
    total_overtime += overtime_pay
    total_regular += regular_pay
    total_gross += gross_pay
    
    # Print individual employee details
    print("\n--- Employee Pay Details ---")
    print(f"{'Employee Name:':<20}{employee_name:<15}")
    print(f"{'Hours Worked:':<20} {'Pay Rate:':<15} {'Overtime:':<15} {'Overtime Pay:':<15} {'Regular Pay:':<15} {'Gross Pay:':<10}")
    print("-" * 95)
    print(f"{hours_worked:<20.2f} ${pay_rate:<15.2f} {overtime_hours:<15.2f} ${overtime_pay:<15.2f} ${regular_pay:<15.2f} ${gross_pay:<20.2f}")

# Print final summary
print("\n=== Final Company Summary ===")
print(f"Total Number of Employees: {employee_count}")
print(f"Total Overtime Pay: ${total_overtime:.2f}")
print(f"Total Regular Pay: ${total_regular:.2f}")
print(f"Total Gross Pay: ${total_gross:.2f}")