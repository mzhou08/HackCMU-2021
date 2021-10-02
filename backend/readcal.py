from icalendar import Calendar, Event

# To access the encoded datetime values
from icalendar import vDatetime
from datetime import datetime


calName = input("Put the name of your calendar file here:\n")

g = open(calName,'rb')
gcal = Calendar.from_ical(g.read())
for component in gcal.walk():
    if component.name == "VEVENT":
        print(component.get('summary'))
        print(component.get('dtstart').dt)
        print(component.get('dtend').dt)
        print(component.get('dtstamp').dt)
g.close()


def setUpDatabase():
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/calendar.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Calendars 
    (id INTEGER PRIMARY KEY, 
    deck TEXT, 
    front TEXT UNIQUE, 
    back TEXT)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Users 
    (id INTEGER PRIMARY KEY, name TEXT UNIQUE)''')

    conn.commit()
    
    return cur, conn