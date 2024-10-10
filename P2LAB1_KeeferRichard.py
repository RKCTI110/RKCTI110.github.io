#CTI 110
#P2LAB1
#KeeferR
#10/10/2024

# This program adds up sales of something

print("Hello, What is your name? ")
name = input()
print("Welcome", name, "How many tickets would you like?")
number = int(input())
print("Great!", number, "tickets.")
print("How much would you like each ticket to cost?" )
price = float(input())
total = number*price
print("-----Total-----")
print(number, "tickets @ $",price, "is $",total)
print("NC Sales tax @ 4.75%")
tax = .0475
print("Grand total is $", tax*total+total)
