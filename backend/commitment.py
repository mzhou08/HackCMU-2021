class Commitment():
    def __init__(self, time, name, deadline):
        self.time = time
        self.name = name
        self.deadline = deadline
    def getTime(self):
        return self.time
    def getName(self):
        return self.name
    def setTime(self, newTime):
        self.time = newTime
    def getDeadline(self):
        return self.deadline
