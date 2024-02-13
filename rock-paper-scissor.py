rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
'''
Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.
'''
import random
user_input = int(input("Kindly Enter your choice?\n0 - Rock\n1 - Paper\n2 - Scissors\n"))
if user_input > 2 or user_input < 0:
    print("You enter an invalid number and you loose ...")
else:
    rps = ['rock', 'paper', 'Scissors']
    print(f'User"s Choose: {rps[user_input]}')
    if user_input == 0:
        print(rock)
    elif user_input == 1:
        print(paper)
    elif user_input == 2:
        print(scissors)

    computers_choice = random.randint(0,2)
    computer_choose = rps[computers_choice]

    print(f'Computer"s Choose: {computer_choose}')
    if computers_choice == 0:
        print(rock)
    elif computers_choice == 1:
        print(paper)
    elif computers_choice == 2:
        print(scissors)

    if user_input == 0 and computers_choice == 2:
        print("You Win!")
    elif user_input == 1 and computers_choice == 0:
        print("You Win!")
    elif user_input == 2 and computers_choice == 1:
        print("You Win!")
    elif user_input == 2 and computers_choice == 0:
        print("Computer Win!")
    elif user_input == 1 and computers_choice == 2:
        print("Computer Win!")
    elif user_input == 0 and computers_choice == 1:
        print("Computer Win!")
    else:
        print("Draw ..")
