from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []  # empty list to store the questions

for data in question_data:
    # print(data['text'])
    # print(data['answer'])
    new_question = Question(data['question'], data['correct_answer'])
    # print(new_question.text, new_question.answer)
    question_bank.append(new_question)

# print(len(question_bank)) # to double confirm if 12 questions were added into the list
# print(question_bank[0].text, question_bank[0].answer) # to print out the question bank index.text or .answer

quiz = QuizBrain(question_bank)
# print(questions.question_list[0].text)
while quiz.still_has_questions():
    quiz.next_question()
    if quiz.still_has_questions() == False:
        print("You completed the quiz.")
        print(f"Your final score is {quiz.score}/{quiz.question_no}.")
