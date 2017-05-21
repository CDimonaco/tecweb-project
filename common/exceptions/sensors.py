class SensorErrors(Exception):
    pass

class SensorNotFoundError(SensorErrors):
    def __init__(self):
        super(SensorNotFoundError, self).__init__("Sensor not found")


class SensorAddError(SensorErrors):
    def __init__(self):
        super(SensorAddError, self).__init__("Error adding the sensor")
