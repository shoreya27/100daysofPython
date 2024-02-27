from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question_bank.append(Question(text=data['text'],
                                  answer=data['answer']))
qz = QuizBrain(question_list=question_bank)

while qz.still_has_question():
    qz.next_question()

print('You have completed the Quiz.')
print(f'Your final score is: {qz.score}/{qz.question_number}')