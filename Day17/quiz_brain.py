class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def remaining_question(self):
        # number_of_qs = len(self.question_list)
        # if number_of_qs > self.question_number:
        #     return True
        # else:
        #     return False
        #Better way to write it

        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):")
        self.check_answer(answer,current_question.answer)

    def check_answer(self, response, answer):
        if response.lower() == answer.lower():
            self.score += 1
            print("Nice you got it right!")
        else:
            print("Uh oh that was wrong.")
        print(f"Your current score is {self.score}/{self.question_number}\n")



