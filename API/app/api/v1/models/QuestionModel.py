import uuid
from datetime import datetime

questions = []

class Question(object):
    """This class represents the Model for Question(s)"""
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
            "answered":self.answered
        }
        #Add to list
        questions.append(question)
        return question

    def update_question(self,questionid: str,question_update):
        #find the question
        index, question = self.find_question(questionid)
        if iter(question):
            question["title"] = question_update["title"]
            question["body"] = question_update["body"]
            question["tags"]  = question_update["tags"]

            questions[index] = question
            return question

    def delete_question(self, questionid: str):
        #find question
        index, _ =  self.find_question(questionid)
        if index:
            questions.pop(index)
            return True

    def find_question(self,questionid: str):
        if iter(questions):
            for index,question in enumerate(questions):
                if question["questionid"] == questionid:
                    return index, question
        else:
            return None, None
    
    def get_questions(self):
        return questions

    def find_user_questions(self, userid: str):
        userquestions = []
        for question in questions:
            if question['userid'] == userid:
                userquestions.append(question)

        return userquestions
