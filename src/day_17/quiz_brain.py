from src.day_17.question_model import Question


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.user_score = 0

    def next_question(self):
        """ Asking the questions"""
        question_text: str = self.question_list[self.question_number].text
        question_answer: str = self.question_list[self.question_number].answer

        self.check_answer(input(f"Q.{self.question_number + 1}: {question_text} (True/False)?: "),
                          question_answer)
        print("\n")

    def still_has_questions(self) -> bool:
        """ Checking if we are at the end of the quiz"""
        return self.question_number < len(self.question_list)


    def check_answer(self, user_answer: str, correct_answer: str) -> None:
        """ Checking if the answer was correct"""
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!" )
            self.user_score += 1
        else:
            print("That's wrong")
        self.question_number += 1
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: ({self.user_score}/{self.question_number})")