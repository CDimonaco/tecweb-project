class UserErrors(Exception):
    pass

class UserNotFoundError(UserErrors):
    def __init__(self):
        super(UserNotFoundError, self).__init__("User not found")


class UserAddError(UserErrors):
    def __init__(self):
        super(UserAddError, self).__init__("Error adding the user")
