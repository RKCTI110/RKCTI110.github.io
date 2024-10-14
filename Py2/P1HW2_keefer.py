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
print(f'{"Location:":<30} {destination}')
print(f'{"Initial Budget:":<30} ${budget:.2f}')
print(f'{"Fuel:":<30} ${fuel:.2f}')
print(f'{"Hotel:":<30} ${hotel:.2f}')
print(f'{"Food:":<30} ${food:.2f}')

print(f'{"Total Expenses:":<30} ${fuel + hotel + food:.2f}')
print("------------------")

print('Remaining Balance: ', '$' + format(budget -  total, '.2f'))


#print(f'{number:.2f}')


#sub expenses

#results