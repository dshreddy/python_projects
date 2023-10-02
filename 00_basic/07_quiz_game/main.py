from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


# A question bank of question objects
q_bank = [Question(dic["text"], dic["answer"]) for dic in question_data]

# A quiz object
quiz_obj = QuizBrain(q_bank)

while quiz_obj.still_has_questions():
    quiz_obj.next_question()
    ans = input()
    quiz_obj.check_ans(ans)
    print(f"Your score : {quiz_obj.score}/{quiz_obj.question_number}")






