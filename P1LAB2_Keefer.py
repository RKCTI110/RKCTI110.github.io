# CTI110
# P1LAB2 - Receipt
# Keefer
#10/1/24

print("P1LAB2")


num_burgers = 0
num_fries = 0
burger_cost = 4.99
fry_cost = 0.99

print("Can I take your order?")
#Have to convert their input to an INT
num_burgers = int(input("How many burgers?"))

print("You ordered", num_burgers, "burgers")

print("Anything else?")

num_fries = int(input("Sure, How many fries would you like?"))

print("Of course, 3 burgers and 4 fries")

burger_total = num_burgers * burger_cost
fry_total = num_fries * fry_cost
meal_total = burger_total + fry_total

print("-" * 20)
print(num_burgers, "burger\t$", burger_total)
print(num_fries, "fry\t\t$", fry_total)
print("-" * 20)
print("Total\t\t$", meal_total)




