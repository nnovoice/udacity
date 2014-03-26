# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#
debug = False
#debug = True

days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    if ((year % 4) == 0):
        if ((year % 100) == 0):
            if ((year % 400) != 0):
                return False
            else:
                return True
        else:
            return True
    return False
        
def getNextDay(year, month, day):
    next_year = year
    next_month = month
    next_day = day
    
    num_days = days_in_month[month]
    if debug == True:
        print 'month=', month, 'num_days=', num_days
    if (day == num_days):
        if (month == 2 and isLeapYear(year) == True):
            if debug == True:
                print 'month=', month, 'leap year=', True
            next_day = 29
        else:
            if (month == 12):
                next_day = 1
                next_month = 1
                next_year += 1
            else:
                next_day = 1
                next_month = next_month + 1
    else:
        if (month == 2 and isLeapYear(year) == True and day > num_days):
            next_day = 1
            next_month += 1
            if debug == True:
                print 'Month is Feb in a leap year and days are > 28, so next day=', next_year, next_month, next_day
        else:
            next_day += 1

    if debug == True:
        print 'Next date=', next_year, next_month, next_day
    return (next_year, next_month, next_day)
    

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    numDays = 0
    nextDate = (year1, month1, day1)
    while nextDate != (year2, month2, day2):
        numDays += 1
        if debug == True:
            print numDays
        #print nextDate[0], nextDate[1], nextDate[2]
        nextDate = getNextDay(nextDate[0], nextDate[1], nextDate[2])
    
    return numDays


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed", 'got=', result, 'expected', answer
        else:
            print "Test case passed!"


print 'Next day of ', (2012, 2, 28), getNextDay(2012, 2, 28), 'result=', getNextDay(2012, 2, 28) == (2012, 2, 29)
print 'Next day of ', (2012, 2, 29), getNextDay(2012, 2, 29), 'result=', getNextDay(2012, 2, 29) == (2012, 3, 1)
print 'Next day of ', (2012, 2, 25), getNextDay(2012, 2, 25), 'result=', getNextDay(2012, 2, 25) == (2012, 2, 26)
print 'Next day of ', (2013, 2, 28), getNextDay(2013, 2, 28), 'result=', getNextDay(2013, 2, 28) == (2013, 3, 1)
print 'Next day of ', (2000, 2, 28), getNextDay(2000, 2, 28), 'result=', getNextDay(2000, 2, 28) == (2000, 2, 29)

test()
#print daysBetweenDates(2012,1,1,2012,2,28)
#print daysBetweenDates(2012,1,1,2012,3,1)
