SCOREPERQuestion = 1
TOTALNUMBR = 12 * SCOREPERQuestion

class QuizeBrain:
    def __init__(self, qlist):
        self.questionNumber = 0
        self.questionList = qlist
        self.score = 0


    def still_have_queston(self):
        if self.questionNumber < len(self.questionList):
            return True
        else:
            return False
    def nextQuestion(self):
        current_question = self.questionList[self.questionNumber]
        self.questionNumber += 1
        useranswer = input(f"Q {self.questionNumber} :  {current_question.text} (True/False): ")
        # print(f"Q: {self.questionList[0].text}")
        self.checkAnswer(useranswer, current_question.answere)

    def checkAnswer(self, useranswer, corectanswer):
        if useranswer.lower() == corectanswer.lower() :
            self.score += SCOREPERQuestion
            print("You got correct answer")
        else:
            print("You got wrong answer")
            self.score -= 0.25
        print(f"The correct Answer Was: {corectanswer}")
        print(f"Your Current Score is: {self.score}/{TOTALNUMBR}")