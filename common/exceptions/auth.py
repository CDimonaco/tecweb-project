class AuthErrors(Exception):
    pass

class RegisterSameUserError(AuthErrors):
    def __init__(self):
        super(RegisterSameUserError, self).__init__("Utente già presente con queste credenziali")


