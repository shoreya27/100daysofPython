# Fizz Buzz FizzBUZZ

print('!! FIZZBUZZ ARENA !!')

# Rules
# print number from 1 to 100
# print Fizz when number is divisible by 3
# print Buzz when number is divisible by 5
# print FizzBuzz when number is divisible by 15

for i in range(1, 101):
    if i % 15 == 0:
        print('FIZZBUZZ')
    elif i % 3 == 0:
        print('FIZZ')
    elif i % 5 == 0:
        print('BUZZ')
    else:
        print(i)