from flask import request, jsonify, abort, make_response, session
from flask import Blueprint

from ..models.UserModel import users,User
from ..utils.validator import password_match,set_password,check_password


auth = Blueprint('auth',__name__, url_prefix='/api/v1')

@auth.route('/register', methods=['POST'])
def register():
    '''register a user to the platform'''
    if request.get_json():
        data = request.get_json()
        username = data['username']
        email = data['email']
        password = data['password']
        confirm_password = data['confirm_password']
        
        if password_match(password, confirm_password):
            '''Add user to the data structure'''
            pswdhash = set_password(password)
            user = User(email,username,pswdhash).add_user()

            session['userid'] = user['userid']
            response =jsonify(user)

            response.status_code = 201
            return response
        else:
            abort(make_response(jsonify({"message":"Passwords don't match"}),400))

    else:
        abort(make_response(jsonify({"message":"POST of type Application/JSON expected"}),400))
    

@auth.route('/login', methods=['POST'])
def login():
    '''login a user to the platform'''
    if request.get_json():
        data = request.get_json()
        username = data['username']
        password = data['password']

        find_usr = User().find_user(username)
        if find_usr:
            '''Check password match'''
            if check_password(find_usr['password'],password):
                if not session.get('userid'):
                    session['userid'] = find_usr['userid']
                return make_response(jsonify({"message":"Successfully Logged In"}),200)
            else:
                abort(make_response(jsonify({"message":"Invalid Password"}),400))
        else:
            abort(make_response(jsonify({"message":"User not Found"}),404))