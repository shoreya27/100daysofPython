# Get the highest score from a given list

scores = [78, 65, 89, 86, 55, 91, 64, 89]

res = -9999

for score in scores:
    if res < score:
        res = score

print(f'The highest score in the class is: {res}')