class quizbrain:
    def __init__(self,q_list):
        self.question_number= 0
        self.question_list= q_list

    def next_question (self):
        currrent_question = self.question_list[self.question_number]
        input(f"Q.{self.question_number}: {currrent_question.text} (True/False)")