def check_prime(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is Prime.")
    else:
        print(f"{number} is not Prime.")

number = int(input("Please enter your number ? "))

check_prime(number=number)
