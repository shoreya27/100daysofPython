# Python Calculator
from art import logo

print(logo)
print()
def add(num1, num2):
    """
    returns Num1 + Num2
    """
    return num1 + num2

def subtract(num1, num2):
    """
    returns Num1 - Num2
    """
    return num1 - num2

def multiply(num1, num2):
    """
    returns Num1 * Num2
    """
    return num1 * num2

def divide(num1, num2):
    """
    returns Num1 / Num2
    """
    return num1 / num2

operations = {
    '+' : add,
    '-' : subtract,
    '/' : divide,
    '*' : multiply
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the Second number?: "))

def show_operations():
    for operation in operations:
        print(f'{operation} - {operations[operation].__name__}')

def get_answer(num1, num2):
    symbol = input("Pick an operation from the line above: ")
    function = operations[symbol]
    answer = function(num1=num1, num2=num2)
    print(f'{num1} {symbol} {num2} = {answer}')
    return answer

show_operations()
answer = get_answer(num1, num2)
print()
keep_going = True
while keep_going:
    going = input(f"Do you want to continue operations with previous answer {answer}, type 'y' for yes: ")
    print()
    if going != 'y':
        break
    num = int(input("What's the next number?: "))
    show_operations()
    new_answer = get_answer(num, answer)
    answer = new_answer
