# Solution 1 Using Datetime Module
'''from datetime import datetime
date="oct 14 1997 7:45AM"
print(type(date))
date_time=datetime.strptime(date, "%b %d %Y %I:%M%p")
print(date_time)
print(type(date_time))'''

# Solution 2 Using datetil Module
from dateutil import parser
date_time=parser.parse("oct 14 1997 7:45AM")
print(date_time)
print(type(date_time))