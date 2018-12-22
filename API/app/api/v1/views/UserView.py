from flask import request, jsonify, abort, make_response
from flask import Blueprint

from ..models.UserModel import users,User
from ..utils.validator import password_match


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
            user = User(email,username,password)
            user.add_user()
            return make_response(jsonify({"message":"Successfully Registered"}),201)
        else:
            abort(400, 'Password and Confirm Password don\'t match')
    else:
        abort(400,"application/json expected")
    

@auth.route('/login', methods=['POST'])
def login():
    '''login a user to the platform'''
    if request.get_json():
        data = request.get_json()
        username = data['username']
        password = data['password']

        user = User()
        find_usr = user.find_user(username)
        if find_usr:
            '''Check password match'''
            if user.check_password(find_usr['password'],password):
                return make_response(jsonify({"message":"Successfully Logged In"}),200)
            else:
                abort(400,"Invalid Password")
        else:
            return make_response(jsonify({"message":"User not Found"},404))