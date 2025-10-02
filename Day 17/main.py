from question_model import question
from data import question_data
from quiz_brain import quizbrain
question_bank=[]
for question in question_data:
    question_text =  question["text"]
    question_ans=question["answere"]
    new_question = question(question_text,question_ans)
    question_bank.append(new_question)

quiz = quizbrain(question_bank)
quiz.next_question()