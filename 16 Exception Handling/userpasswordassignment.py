class InvalidPasswordException(Exception):
    def __init__(self, msg):
        self.msg = msg

def enterPWD(password):

    if(len(password)<8):
        raise InvalidPasswordException("You have to enter a password of minimum length of 8 characters")

enterPWD("anubhav")