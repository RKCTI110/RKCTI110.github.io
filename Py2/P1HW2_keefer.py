# Keefer_R
# 10/08/2024
# P1HW2
# Creating a budget for trip


print('🎃 Trip Calculator 🦇')

budget = float(input("What is your travel budget? $"))
#Where
destination = input("Where are you going? ")
#fuel
fuel = float(input("How much do you need for gas both ways? "))
#accommodation
hotel = float(input("How much is the total (include taxes and fees) for hotel stay? "))
#food
food = float(input("Estimate how much you'll need for ALL meals during trip. Don't forget travel days! "))

total = fuel + hotel + food

print('🧛 ----------Travel Expenses---------- 🕸️')
#add expenses
print('Location:', destination)
print('Initial Budget: ', '$' + format(budget, '.2f'))

print({['Fuel:'] :<15}, '$' + format(fuel, '.2f'))
print({['Hotel:'] :<15}, "$" + format(hotel, ".2f"))
print({['Food:'] :<15,} '$' + format(food, ".2f"))

print({['Total Expenses:']:<15}, '$' + format(fuel + hotel + food, '.2f'))
print("------------------")

print('Remaining Balance: ':<35, '$' + format(budget -  total, '.2f'))





#sub expenses

#results