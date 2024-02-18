student_score = {
    "Harry": 81,
    "Ron": 78,
    "Hermoine": 99,
    "Draco": 74,
    "Neville": 62
}

student_grade = {}

for student in student_score:
    score = student_score[student]
    if score >= 91:
        student_grade[student] = 'Outstanding'
    elif score >= 81:
        student_grade[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grade[student] = 'Acceptable'
    else:
        student_grade[student] = 'Fail'

print(student_grade)