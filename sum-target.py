# Sum upto given target only even number

target = int(input('Target Value(0-1000): '))

sum = 0
for i in range(0, target+1, 2):
    sum += i

print(f'Sum of even numbers till {target} is {sum}')