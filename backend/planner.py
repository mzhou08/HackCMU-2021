class Planner():

    def __init__(self, events, commitments):
        self.events = events
        self.commitments = commitments
        self.calendar = AllocCal("", "planner")
        
    def addEvent(self, e):
        self.events.append(e)

    def addCommitment(self, c):
        self.commitments.append(c)

    def allocate_commitments():
        
        
