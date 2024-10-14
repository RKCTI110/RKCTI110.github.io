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
print('Initial Budget: $', budget)

print('Fuel: $', format(fuel, '.2f'))
print('Hotel: $', hotel)
print('Food: $', food)

print('Total Expenses: $', fuel + hotel + food)
print("------------------")

print('Remaining Balance: $', budget -  total)





#sub expenses

#results