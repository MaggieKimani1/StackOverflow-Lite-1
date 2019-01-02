from flask import request, session, make_response, abort, jsonify
from flask import Blueprint
from ..models.QuestionModel import Question, questions

ques = Blueprint('ques', __name__, url_prefix="/api/v1")

@ques.route('/question/<id>', methods=['GET'])
def get_question(id: str):
    '''GET a particular question using the Id'''
    _, ques = Question.find_question(id)
    if ques:
        _, question = Question.find_question(id)
        response = jsonify(question)
        response.status_code = 200
        return response
    else:
        abort(make_response(jsonify({"message":"Not Found"}),404))

@ques.route('/questions', methods=['GET'])
def get_all():
    '''GET all questions'''

    response = jsonify(Question.get_questions())
    response.status_code = 200
    return response

@ques.route('/userquestions/<id>', methods=['GET'])
def get_user_questions(id: str):
    response = jsonify(Question.find_user_questions(id))
    response.status_code = 200
    return response

@ques.route('/question', methods=['POST'])
def post_question():
    '''POST a question'''

    if request.get_json():
        data = request.get_json()
        title = data['title']
        body = data['body']
        tags = data['tags']
        userid = session.get('userid')    
        #add items
        try:
            question = Question(title,body,tags,userid).add_question()
            response = jsonify(question)
            response.status_code = 201
            return response
        except:
            abort(make_response(jsonify({"error":"Unexpected error"}),500))
    else:
        abort(make_response(jsonify({"message":"POST of type Application/JSON expected"}),400))

@ques.route('/question/<id>', methods=['PUT'])
def put_question(id: str):
    '''PUT / Update a question'''

    if request.get_json():
        data = request.get_json()
        try:
            #update
            question = Question.update_question(id,data)
            response = jsonify(question)
            response.status_code = 202
            return response
        except:
            abort(make_response(jsonify({"message":"Not Found"}),404))
    else:
        abort(make_response(jsonify({"message":"POST of type Application/JSON expected"}),400))

@ques.route('/question/<id>', methods=['DELETE'])
def delete_question(id: str):
    '''DELETE question'''
    _, ques = Question.find_question(id)
    if ques:
        Question.delete_question(id)
        return make_response(jsonify({"message":"Successfully deleted"}),204)
    else:
        abort(make_response(jsonify({"message":"Not found"}),404))
