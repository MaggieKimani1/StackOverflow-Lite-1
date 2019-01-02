import uuid
from datetime import datetime
from .QuestionModel import Question

answers = []
class Answer(Question):
    
    '''This is the Answer Model, handles CRUD operations for Answers'''

    def __init__(self, questionid, answerbody= '', userid = '', votes = 0, isapproved = False ):
        '''Initializer Expects questionid'''
        super().__init__(self)

        self.answerid = uuid.uuid4().hex
        self.questionid = questionid
        self.body = answerbody
        self.userid = userid
        self.votes = votes
        self.isapproved = isapproved
        self.timestamp = datetime.now()

    def add_answers(self):
        '''adds the Answer to th data structure'''
        answer = {
                    self.questionid:
                    {
                        "answerid": self.answerid,
                        "body":self.body,
                        "userid":self.userid,
                        "time":self.timestamp,
                        "votes":self.votes,
                        "isapproved": self.isapproved
                    }
                }
        answers.append(answer)
        return answer

    def add_answer_to_question(self, ques: list):
        '''Expects provided with question list'''
        ques["answers"].append(self.answerid)
        update_ques = super().update_question(ques["questionid"], ques)
        return update_ques