from werkzeug.security import generate_password_hash, check_password_hash

#global variable
users =[]

class User(object):    
    '''This class initializes User Model and Stores User Credential'''
    
    def __init__(self, email=None, username=None, password=None):
        self.user_id = len(users)+1
        self.email = email
        self.username = username
        self.set_password(password)

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, passwd_hash, password):
        return check_password_hash(passwd_hash,password)

    def add_user(self):
        user = {
            "userid": self.user_id,
            "email": self.email,
            "username": self.username,
            "password":self.password_hash
        }
        users.append(user)
        return users

    def get_users(self):
        return users

    def find_user(self,username):
        for user in users:
            if user['username'] == username:
                return user
