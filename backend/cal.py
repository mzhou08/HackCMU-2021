from icalendar import Calendar, Event

# To access the encoded datetime values
from icalendar import vDatetime

import os
import sqlite3
import datetime
import pytz

class AllocCal():
    def __init__(self, calName, user):

        '''FIX THIS LATER'''
        self.utc = pytz.UTC


        self.calName = calName
        self.user = user
        self.events = []
        # Initialize the Database
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.conn = sqlite3.connect(self.path+'/calendar.db')
        self.cur = self.conn.cursor()

        self.cur.execute('''CREATE TABLE IF NOT EXISTS Calendars 
        (id INTEGER PRIMARY KEY, 
        user_id INTEGER,
        title TEXT, 
        start TEXT,
        end TEXT)''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS Users 
        (id INTEGER PRIMARY KEY, name TEXT UNIQUE)''')

        self.conn.commit()

        self.cur.execute("SELECT name FROM Users WHERE name = ?", (self.user,))

        if (self.cur.fetchone() == None):
            self.cur.execute("INSERT INTO Users (name) VALUES (?)", (self.user,))

            self.conn.commit()

        self.cur.execute("SELECT id FROM Users WHERE name = ?", (self.user,))

        self.userID = self.cur.fetchone()[0]

        # Read the ICS file
        if self.calName != "":
            with open (self.calName,'rb') as g:
                self.gcal = Calendar.from_ical(g.read())
                for component in self.gcal.walk():
                    if component.name == "VEVENT":
                        title = component.get('summary')
                        start = component.get('dtstart').dt
                        end = component.get('dtend').dt
                    
                        # Get current timestamp
                        #component.get('dtstamp').dt

                        self.events.append([self.userID, title, start, end])

            self.conn.commit()

        self.events = sorted(self.events, key = lambda x: x[2])

        # print(self.events)


    def writeToDB(self):
        # If the user wants to import a calendar
        if self.calName != "":
        
            for event in self.events:
                self.conn.execute("INSERT INTO Calendars (user_id, title,start,end) VALUES (?,?,?,?)", (event[0], event[1], event[2], event[3]))
            
            self.conn.commit()


    # def writeToICal(self):
    #     self

    def getEvents(self):
        return self.events

    def sortEvents(self):
        self.events = sorted(self.events, key = lambda x: x[2])

    def addEvent(self, e):
        self.events.append(e)

    def getFreeBlocks(self):
        blocks = []
        relevant = []
        oneHour = datetime.timedelta(hours = 1)
        for e in self.events:
            if e[3].replace(tzinfo = self.utc) < datetime.datetime.now().replace(tzinfo = self.utc):
                relevant.append(e)

        for i in range(len(relevant) - 1):
            blockStart = relevant[i][3]
            blockEnd = blockStart + oneHour
            while blockEnd < relevant[i+1][2]:
                blocks.append([blockStart, blockEnd])
                blockStart = blockEnd
                blockEnd = blockStart + oneHour
        return blocks

newCal = AllocCal("mhzhou@andrew.cmu.edu.ics", "michael")
print(newCal.getFreeBlocks())
