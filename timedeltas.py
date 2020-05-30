#Example file for working with timedelta objects


from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

#construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

#print today's date
now = datetime.now()
print("Today is: "+str(now))

#print today's date one year from now
print("one year from now, it will be: " +str(now+timedelta(365)))

#create a timedelta that uses more than one arguement
print("In 2 days and 3 weeks , it will be " +str(now+timedelta(days=2,weeks=3)))

#calculate the date 1 week ago, formatted as string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("One week ago, it was: "+s)

#how many days until April Fools Day?
today = date.today()
afd = date(today.year, 4, 1)

if afd < today:
    print("April Fools day already went by %d days ago" % ((today-afd).days))
    afd = afd.replace(year = today.year+1)

#Now calculate the amount of time until next April Fools day
time_to_afd = afd - today
print("Its just ", time_to_afd.days, "days until April Fools day")