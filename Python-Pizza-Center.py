# Pizza Delivery center
print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want ? S, M, or L\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25

if add_pepperoni == 'Y':
    bill += 2

if extra_cheese == 'Y':
    bill += 1

print(f"Your final bill is: ${bill}")