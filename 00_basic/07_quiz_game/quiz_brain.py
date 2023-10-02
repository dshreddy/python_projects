class QuizBrain:
    def __init__(self, q_bank):
        self.question_number = 0
        self.question_list = q_bank
        self.score = 0

    def next_question(self):
        # A question object
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"Q.{self.question_number}: {current_question.question} (True/False) :")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_ans(self, ans):
        current_question = self.question_list[self.question_number-1]
        if ans == current_question.answer:
            self.score += 1

