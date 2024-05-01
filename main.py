#impoting data
from question_modal import Question
from quize_brain import QuizeBrain
from data import dataDB
question_bank = []

for question in dataDB:
    # print(question)
    questiontext = question["question"]
    questionAnswer = question["correct_answer"]
    new_question = Question(questiontext, questionAnswer)
    # print(questiontext,questionAnswer)
    question_bank.append(new_question)


newquize = QuizeBrain(question_bank)
while newquize.still_have_queston():
    newquize.nextQuestion()

# print(question_bank[0].answere)
