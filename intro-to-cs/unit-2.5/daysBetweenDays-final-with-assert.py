# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Compensate for leap days.
# Assume that the birthday and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is 2 Jan 2012
# you are 1 day old.
#
# Hint
# A whole year is 365 days, 366 if a leap year.

def isLeapYear(year):
	if ((year % 4) == 0):
	   if ((year % 100) == 0):
		if ((year % 400) == 0):
		  return True
		else:
		  return False
	   else:
	       return True
	return False

days_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def nextDay(year, month, day):
    if day < days_in_months[month]:
        return year, month, day + 1
    else:
		if (month == 2 and isLeapYear(year)):
			if (day == 28):
				return year, month, day + 1
			else:
				return year, month + 1, 1

		if (month < 12):
			return year, month + 1, 1
		if (month == 12):
			return year + 1, 1, 1
		else:
			return year, month + 1, 1

def dateIsAfter(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is after year2-month2-day2.  Otherwise, returns False."""

    if year1 > year2:
        return True
    if year1 == year2:
        if month1 > month2:
            return True
        if month1 == month2:
            return day1 > day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""

    # program defensively! Add an assertion if the input is not valid!
    assert(dateIsAfter(year2, month2, day2, year1, month1, day1))

    days = 0
    while dateIsAfter(year2, month2, day2, year1, month1, day1):
        days += 1
        (year1, month1, day1) = nextDay(year1, month1, day1)
    return days
	
def testLeapYear():
	test_cases = [(2004, True), (2000, True), (3000, False), (2012, True)]
	for (year, answer) in test_cases:
		result = isLeapYear(year)
		if (result == answer):
			print "Test with year= ", year, "passed"
		else:
			print "Test failed."

def testNextDay():
	test_cases = [((2004, 1, 1),(2004, 1, 2)),
		      ((2004, 2, 28),(2004, 2, 29)),
		      ((2004, 2, 29),(2004, 3, 1)),
		      ((2004, 12, 31),(2005, 1, 1)),
		      ((1980, 11, 29),(1980, 11, 30)),		      
		      ((2007, 2, 25),(2007, 2, 26)),		      
		      ((2007, 2, 28),(2007, 3, 1)),
	      
		      ]

	for (args, answer) in test_cases:
		result = nextDay(*args)
		if result != answer:
			print "Test with data:", args, "failed", " got ", result
		else:
			print "Test with data:", args, "with expected=", answer, " passed!"

def test():
    test_cases = [((2012,9,30,2012,10,30),30),
                  ((2012,1,1,2013,1,1),366),
                  ((2012,9,1,2012,9,4),3),
				  ((2012,1,1,2012,2,28), 58), 
				  ((2012,1,1,2012,3,1), 60),
				  ((2011,6,30,2012,6,30), 366),
				  ((2011,1,1,2012,8,8), 585 ),
				  ((1900,1,1,1999,12,31), 36523),
				  ((2013,1,1,1999,12,31), "AssertionError"),]

    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result != answer:
                print "Test with data:", args, "failed", " got this= " , result, " instead of: ", answer
            else:
                print "Test case passed!"
        except AssertionError:
            if answer == "AssertionError":
                print "Nice job! Test case {0} correctly raises AssertionError!\n".format(args)
            else:
                print "Check your work! Test case {0} should not raise AssertionError!\n".format(args)
test()
testNextDay()
testLeapYear()
