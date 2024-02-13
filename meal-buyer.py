# Party Thrower Random
import random
names = input("Enter names of party goer's? ").split(', ')
print(names)

surprise = random.randint(0, len(names)-1)
print(f'{names[surprise]} is going to buy the meal today!')