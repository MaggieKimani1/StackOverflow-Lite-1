from flask import request, make_response, abort, session, jsonify
from flask import Blueprint

from ..models.AnswerModel import Answer 

ans = Blueprint('ans', __name__, url_prefix='/api/v1')

@ans.route('/answer/<id>', methods=['POST'])
def post_answer(id: str):
    if request.get_json():
        
        data = request.get_json()
        answer_body = data['body']
        answer_votes = data ['votes']
        answer_isapproved = data['isapproved']
        userid_ = session.get('userid')

        ans_object = Answer(id,answer_body,userid_,answer_votes,answer_isapproved)

        if ans_object.find_question(id):
            try:
                answer = ans_object.add_answers()
                response = jsonify(answer)
                response.status_code = 201
                return response
            except Exception as e:
                abort(make_response(jsonify({"message":"Error {}".format(e)}),500))
        else:
            abort(make_response(jsonify({"message":"Not found"}), 404))

    else:
        abort(make_response(jsonify({"message":"POST of type Application/JSON expected"}),400))