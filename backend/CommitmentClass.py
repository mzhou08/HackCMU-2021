class Commitment():
    def __init__(self, time, name):
        self.time = time
        self.name = name
    def getTime(self):
        return self.time
    def getName(self):
        return self.name
    def setTime(self, newTime):
        self.time = newTime