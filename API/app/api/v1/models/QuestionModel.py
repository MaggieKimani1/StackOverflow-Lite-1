import uuid

questions = []
class Question(object):
    """This class represents the Model for Question(s)"""
    def __init__(self,questiontitle: str, questionbody: str, questiontags: list):
        self.questionid = uuid.uuid4().hex
        self.questiontitle = questiontitle
        self.questionbody = questionbody
        self.questiontags = questiontags

    def add_question(self):
        question = {
            "questionid": self.questionid,
            "title": self.questiontitle,
            "body": self.questionbody,
            "tags":self.questiontags
        }
        #Add to list
        questions.append(question)
        return question

    def update_question(self,questionid: str,question_update: dict):
        #find the question
        index, question = self.find_question(questionid)
        if question:
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
        for index,question in enumerate(questions):
            if question["questionid"] == questionid:
                return index, question
    