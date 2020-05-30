#Examples for working with date information


from datetime import date
from datetime import time
from datetime import datetime

def main():
    ##Date Objects
    # Get today's date from the simple today() method from the date class
    # today = date.today()
    # print("Today's date is ", today)

    # #print out the date's individual components
    # print("Date Components: ", today.day, today.month, today.year)

    # #retrieve today's weekday(0=monday, 6=sunday)
    # print("Today's weekday number is: ", today.weekday())

    ##DateTime Objects
    #Get today's date from datatime calss
    today = datetime.now()
    print("The Current date and time is: ", today)
    
    #Get the current time
    time = datetime.time(datetime.now())
    print("The Current time is: ", time)


main()