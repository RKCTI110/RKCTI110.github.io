# Keefer Richard

# 10/30/2024

# P2HW2

# Grade averages

num1 = float(input("Enter grade for Module 1: "))
num2 = float(input("Enter grade for Module 2: "))
num3 = float(input("Enter grade for Module 3: "))
num4 = float(input("Enter grade for Module 4: "))
num5 = float(input("Enter grade for Module 5: "))
num6 = float(input("Enter grade for Module 6: "))

my_numbers = [num1, num2, num3, num4, num5, num6]

lowest_grade = min(my_numbers)
highest_grade = max(my_numbers)
sum_of_grades = sum(my_numbers)
average = sum_of_grades / len(my_numbers)

print("------------Results------------")
print(f'{"Lowest Grade:":<15} {lowest_grade:.1f}')   
print(f"{'Highest Grade:':<15} {highest_grade:.1f}")
print(f"{'Sum of Grades:':<15} {sum_of_grades:.1f}")  
print(f"{'Average:':<15} {average:.2f}")
print("-------------------------------")
