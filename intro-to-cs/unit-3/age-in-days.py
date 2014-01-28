#plan
# if we are in the same year
    # if we are in the same month
        # return diff of the days
    # else: different month
        # get days in start month
            # get days in month - day
        # get days in end month
            # add end month days
        # add days for the months in between
            # for month + 1 to end month - 1
                # add days
    # add 1 if year is leap and feb 29 got included
# the years are different
    # add days in start year
    # add days in end year
    # add leap days of start year, end year
    # add days for years in between
    # add days for in between leap years

def is_leap_year(y):
    if (y % 4 == 0):
        if (y % 400 == 0):
            return True
        if (y % 100 == 0):
            return False
        return True
    return False

def get_nearest_leap_year(y):
    if (is_leap_year(y) == True):
        return y
    else:
        while (is_leap_year(y) == False):
            y = y + (4 - (y % 4))
        return y

def num_leap_days(y1, y2):
    num_leap_days = 0
    year = get_nearest_leap_year(y1)
    while (year <= y2):
        if (is_leap_year(year)):
            num_leap_days = num_leap_days + 1
        year = year + 4
    return num_leap_days

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def days_in_month(m):
    #print "month= " + str(m - 1) + " days= " + str(months[m - 1])
    return months[m - 1]

#assumption is that (d2, m2, y2) >= (d1, m1, y1)
def age_in_days(d1, m1, y1, d2, m2, y2):
    age = 0

    if (y2 == y1):
        if (m2 == m1):
            return d2 - d1
        else:
            # get days in start month
            age = age + days_in_month(m1) - d1

            # get days in end month
            age = age + d2

            # add days for the months in between
            month = m1 + 1
            end_month = m2 - 1
            while (month <= end_month):
                age = age + days_in_month(month)

            # add 1 if year is leap and feb 29 got included
            if (m1 <= 2 and m2 > 2):
                if (is_leap_year(y1) == True):
                    age = age + 1
    # the years are different
    else:
        # add days in start year
        age = age + days_in_month(m1) - d1
        month = m1 + 1
        while (month < 12):
            age = age + days_in_month(month)
            month = month + 1

        month = 1
        # add days in end year
        while (month < m2):
            age = age + days_in_month(month)
            month = month + 1
        age = age + d2

        # add leap days of start year
        if (is_leap_year(y1) == True):
            if (m1 < 1):
                age = age + 1
            else:
                if (m1 == 2 and d1 <= 29):
                    age = age + 1

        # add leap days of end year
        if (is_leap_year(y2) == True):
            if (m2 > 2):
                age = age + 1
            else:
                if (m2 == 2 and d2 == 29):
                    age = age + 1

        # add days for in between leap years
        years_in_between = y2 - y1 - 1
        if (years_in_between > 0):
            age = 365 * years_in_between
            age = age + num_leap_days(y1, y2)

    return age
# function end

d1, m1, y1 = 25, 2, 2007
d2, m2, y2 = 28, 1, 2014
print age_in_days(d1, m1, y1, d2, m2, y2)

d1, m1, y1 = 25, 2, 2007
d2, m2, y2 = 25, 2, 2007
print age_in_days(d1, m1, y1, d2, m2, y2)

d1, m1, y1 = 25, 2, 2007
d2, m2, y2 = 26, 2, 2007
print age_in_days(d1, m1, y1, d2, m2, y2)

d1, m1, y1 = 25, 2, 2007
d2, m2, y2 = 25, 2, 2008
print age_in_days(d1, m1, y1, d2, m2, y2)

d1, m1, y1 = 25, 2, 2007
d2, m2, y2 = 25, 3, 2008
print age_in_days(d1, m1, y1, d2, m2, y2)

d1, m1, y1 = 25, 2, 2007
d2, m2, y2 = 25, 3, 2008
print age_in_days(d1, m1, y1, d2, m2, y2)

d1, m1, y1 = 29, 2, 2008
d2, m2, y2 = 1, 3, 2008
age = age_in_days(d1, m1, y1, d2, m2, y2)
print age, age == 1

