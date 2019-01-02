import uuid
from datetime import datetime

questions = []

class Question(object):
    """This class represents the Model for Question(s)"""

    answers = []

    def __init__(self,questiontitle = '', questionbody = '', questiontags = [], userid= '', answered = False):
        self.questionid = uuid.uuid4().hex
        self.questiontitle = questiontitle
        self.questionbody = questionbody
        self.questiontags = questiontags
        self.userid = userid
        self.timestamp = datetime.now()
        self.answered = answered

    def add_question(self):
        question = {
            "questionid": self.questionid,
            "title": self.questiontitle,
            "body": self.questionbody,
            "tags":self.questiontags,
            "userid":self.userid,
            "time":self.timestamp,
            "answered":self.answered,
            "answers": self.answers
        }
        #Add to list
        questions.append(question)
        return question

    @classmethod
    def update_question(self,questionid: str,question_update):
        '''Updates Question Expects questionid and question_update of type list'''
        index, question = self.find_question(questionid)
        if iter(question):
            question["title"] = question_update["title"]
            question["body"] = question_update["body"]
            question["tags"]  = question_update["tags"]
            question["answered"] = question_update["answered"]
            question["answers"] = question_update["answers"]
            questions[index] = question
            return question
        return None

    @classmethod
    def delete_question(self, questionid: str):
        '''Deletes Question Expects questionid returns Bool result'''
        index, _ =  self.find_question(questionid)
        if index:
            questions.pop(index)
            return True
        return False
    
    @classmethod
    def find_question(self,questionid: str):
        '''Finds Question expects questionid of type str
            returns question of type list or None tuple
        '''
        if iter(questions):
            for index,question in enumerate(questions):
                if question["questionid"] == questionid:
                    return index, question
        return None,None
    
    @classmethod
    def get_questions(self):
        return questions

    @classmethod
    def find_user_questions(self, userid: str):
        userquestions = []
        for question in questions:
            if question['userid'] == userid:
                userquestions.append(question)

        return userquestions
