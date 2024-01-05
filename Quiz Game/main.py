from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

all_questions = []
for question in question_data:
    new_question = Question(question["question"], question["correct_answer"])
    all_questions.append(new_question)

# Initialize global objects
quiz = QuizBrain(all_questions)
score = 0

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")