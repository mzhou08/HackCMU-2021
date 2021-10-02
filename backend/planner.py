from _typeshed import Self
from cal import AllocCal
from commitment import Commitment

class Planner():

    def __init__(self, commitments, calPath, name):
        self.calendar = AllocCal(calPath, name)
        self.events = self.calendar.getEvents()
        self.commitments = commitments
        
    def addEvent(self, e):
        self.events.append(e)

    def addCommitment(self, c):
        self.commitments.append(c)

    def freeBlocks(self):
        return self.calendar.getFreeBlocks()
        
    def findPriority(self, commitment: Commitment):
        free = self.freeBlocks()
        i = 0

        while free[i][3] < commitment.getDeadline():
            i += 1
        
        if i == 0: 
            print("Not enough time!")
            return 0

        return commitment.getTime() / i

    def findMaxPty(self, commitments):
        highest = [self.findPriority(commitments[0]), 0]
        for i in range(len(commitments)):
            if self.findPriority(commitments[i]) > highest:
                highest = [self.findPriority(commitments[i]), i]

        return highest[1]
    
    def lastFreeBlock(self, commitment, blocks):
        i = len(blocks) - 1

        while blocks[i][3] < commitment.getDeadline():
            i += 1

        return i;

    
    def allocBlocks(self, commitments):
        assigned = dict()
        for i in [c.getName for c in commitments]:
            assigned.get(i,0) = []

        while len(commitments > 0):
            maxPty = self.findMaxPty(commitments)
            maxName = commitments[maxPty].getName()
            lastFree = self.lastFreeBlock(commitments[maxPty], self.freeBlocks())
            if ( len(assigned.get(maxName)) == 0) or ( assigned.get(maxName)[2] > lastFree[3] ):
                assigned[maxName].append(lastFree)
                
            


