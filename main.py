from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for question in question_data:
    q_text = question['text']
    q_answer = question['answer']
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    print(quiz_brain.next_question())

print(
    f"You have completed the quiz. Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")
