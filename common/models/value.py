class Value:
    def __init__(self,id,value,sensor):
        self.id = id
        self.value = value
        self.sensor = sensor

    def __str__(self):
        return "<Value>:"+self.id+self.value+self.sensor

