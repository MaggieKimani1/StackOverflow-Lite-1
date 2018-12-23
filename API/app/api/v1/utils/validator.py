from werkzeug.security import generate_password_hash, check_password_hash

def password_match(password, confirmpass):
    if password == confirmpass:
        return True

def set_password(password):
    password_hash = generate_password_hash(password)
    return password_hash
            
def check_password(passwd_hash, password):
    return check_password_hash(passwd_hash,password)