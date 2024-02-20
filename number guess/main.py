from logo import logo
import random

print(logo)
print("I am thinking of number between 1 - 100.\nPlease guess the number")
print('1 - Hard\n2 - Easy.\nSelect your options below by inputing 1 or 2.')
user_guess = int(input())

if user_guess == 1:
    chances = 5
elif user_guess == 2:
    chances = 10

print(f"You will get {chances} chance to guess the correct number.")
print()
target = random.randint(1, 100)
print(f"target is:{target}")
win = False
while chances > 0:
    user_choose = int(input("Guess no. : "))
    if user_choose > target:
        print("Sorry! Your guess is too high")
    elif user_choose < target:
        print("Sorry! Your guess is too low")
    else:
        print(f"Yes {user_choose} is correct!")
        win = True
        break
    chances -= 1

if not win:
    print("You Loose !!")
else:
    print("You Win !!")