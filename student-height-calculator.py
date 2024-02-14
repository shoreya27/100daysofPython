# Student Heights Calculator
student_heights = input('Enetr all Student Height (cm) Like\n180 200 172 etc\n ').split()

print('Height Avg Calculator')

sum = 0
total_students = len(student_heights)

for height in student_heights:
    sum += int(height)

print('...............')
print(f'Total Students: {total_students}')
print()
print(f'Total Height: {sum}')
print()
print(f'Avg height of students are {round(sum / total_students)}')