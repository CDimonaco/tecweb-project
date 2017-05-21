class ValuesError(Exception):
    pass

class ValueAddError(ValuesError):
    def __init__(self):
        super(ValueAddError, self).__init__("Error adding the value")
        

class ValueNotFoundError(ValuesError):
    def __init__(self):
        super(ValueNotFoundError, self).__init__("Value not found")