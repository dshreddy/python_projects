from tkinter import *
import quiz_brain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, q_brain: quiz_brain.QuizBrain):
        self.quiz_brain = q_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score = 0
        self.score_label = Label(text=f"Score : {self.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="Some text goes here",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_image, highlightthickness=0, command=self.true)
        self.true_btn.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_image, highlightthickness=0, command=self.false)
        self.false_btn.grid(row=2, column=1)

        self.get_q()
        self.window.mainloop()

    def get_q(self):
        if self.quiz_brain.still_has_questions():
            self.canvas.config(bg="White")
            q_txt = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_txt)
        else:
            self.canvas.config(bg="White")
            self.canvas.itemconfig(self.question_text, text="You have reached the end of quiz")

    def true(self):
        if self.quiz_brain.still_has_questions():
            is_right = False
            if self.quiz_brain.current_question.answer:
                self.score += 1
                self.score_label.config(text=f"Score : {self.score}")
                is_right = True

            self.feed_back(is_right)

    def false(self):
        if self.quiz_brain.still_has_questions():
            is_right = False
            if not self.quiz_brain.current_question.answer:
                self.score += 1
                self.score_label.config(text=f"Score : {self.score}")
                is_right = True
            self.feed_back(is_right)

    def feed_back(self, is_right):
        if self.quiz_brain.still_has_questions():
            if is_right:
                self.canvas.config(bg="GREEN")
            else:
                self.canvas.config(bg="RED")
            self.window.after(1000, self.get_q)

