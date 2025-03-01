from src.day_17.question_model import Question
from src.day_17.data import question_data
from src.day_17.quiz_brain import QuizBrain


class QuizProject:

    @classmethod
    def play_game(cls):
        question_bank = \
            [Question(question_obj['text'], question_obj['answer']) for question_obj in question_data]

        quiz = QuizBrain(question_bank)

        while quiz.still_has_questions():
            quiz.next_question()

        print("You've completed the quiz.")
        print(f"Your final score was: ({quiz.user_score}/{quiz.question_number})")