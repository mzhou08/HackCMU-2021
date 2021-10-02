class Event():
    def __init__(self, name, dateAndTime):
        self.name = name
        self.dateAndTime = dateAndTime

    def changeDateTime(self,newDateAndTime):
        self.dateAndTime = newDateAndTime
    
