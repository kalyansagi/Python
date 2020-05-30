#Example file for working with Calendars


import calendar

#create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
# st = c.formatmonth(2020, 1, 0 ,0)
# print(st)

#create an HTML formatted calendar
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# st = hc.formatmonth(2020, 1)
# print(st)

#loop over the days of month
#zeros mean that the day of the week is in overlapping month
# for i in c.itermonthdays(2020, 8):
#     print(i)


 #The Calendar module provides useful utilities for the given locale,
 # such as the names of days and months in full and abbreviated forms.
# for name in calendar.month_name:
#     print(name)  

# for day in calendar.day_name:
#     print(day)


#Calculate days based on a rule: For example, consider a team 
#meeting on the first friday of every month.
#use this script
print("Team meetings will be on: ")
for m in range(1,13):
    cal = calendar.monthcalendar(2020, m)
    weekone = cal[0]
    weektwo = cal[1]
    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]    
    print("%10s %2d" % (calendar.month_name[m], meetday))    
