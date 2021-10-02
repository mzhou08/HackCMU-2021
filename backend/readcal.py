from icalendar import Calendar, Event

# To access the encoded datetime values
from icalendar import vDatetime
from datetime import datetime

g = open('mhzhou@andrew.cmu.edu.ics','rb')
gcal = Calendar.from_ical(g.read())
for component in gcal.walk():
    if component.name == "VEVENT":
        print(component.get('summary'))
        # print(component.get('dtend'))
        # print(component.get('dtstamp'))
g.close()