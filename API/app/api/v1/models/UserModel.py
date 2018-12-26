import uuid
#global variable
users =[]

class User(object):    
    '''This class initializes User Model and Stores User Credential'''
    
    def __init__(self, email=None, username=None, password=None):
        self.user_id = uuid.uuid4().hex
        self.email = email
        self.username = username
        self.password_hash = password

    def add_user(self):
        user = {
            "userid": self.user_id,
            "email": self.email,
            "username": self.username,
            "password":self.password_hash
        }
        users.append(user)
        return user

    def get_users(self):
        return users

    def find_user(self,username):
        for user in users:
            if user['username'] == username:
                return user
