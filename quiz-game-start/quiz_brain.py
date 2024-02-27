
class QuizBrain:

    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f'Q.{self.question_number}: {current_question.text} (True/False)?: ')
        self.check_answer(answer, current_question.answer)
    
    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it Right.")
            self.score += 1
        else:
            print("You got it Wrong.")
        print(f'Correct answer to this question is: {correct_ans.lower()}')
        print(f'Your Score now is: {self.score}/{self.question_number}')
        print('\n')