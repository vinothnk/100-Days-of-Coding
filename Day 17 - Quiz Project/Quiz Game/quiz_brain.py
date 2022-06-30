# TODO 1. asking the questions
# TODO 2. checking if the answer is right
# TODO 3. checking if we are at the end of the quiz


# create a class called QuizBrain
# attributes for QuizBrain
# - question_number to keep track of number of questions asked -> 12 questions inside question_bank
# - questions_list -> to pass through the QuizBrain class

# method for QuizBrain
# next_question() - pulling out the question from the question_bank list

class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q{self.question_no}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
        # item_no = 1
        # points = 0
        #
        # for num in self.question_list:
        #     answer = input(f"Q {item_no}. {self.question_list[self.question_no].text} True/False?: ")
        #     if answer == 'True' and self.question_list[self.question_no].answer == "True":
        #         item_no += 1
        #         points += 1
        #         print(f"You got it right! You scored {points}/ {len(self.question_list)} points.")
        #         self.question_no += 1
        #     elif answer == 'False' and self.question_list[self.question_no].answer == "False":
        #         item_no += 1
        #         points += 1
        #         print(f"You got it right! You scored {points}/ {len(self.question_list)} points.")
        #         self.question_no += 1
        #     else:
        #         item_no += 1
        #         points += 0
        #         print(f"You got it wrong! You scored {points}/ {len(self.question_list)} points.")
        #         self.question_no += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right.")
        else:
            print("You got it wrong.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_no}.")
        print('\n')


