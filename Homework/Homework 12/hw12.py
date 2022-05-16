# Name: Natalie Zoladkiewicz
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS 115 Homework 12

DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''
        Returns a new object with the same month, day, year as the calling
        object (self).
        '''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        '''
        Decides if self and d2 represent the same calendar date, whether
        or not they are in the same place in memory.
        '''
        return self.year == d2.year and self.month == d2.month and self.day == d2.day

    def tomorrow(self):
        '''
        Represents one calendar day after the date it originally represented.
        '''
##        days_in_month = DAYS_IN_MONTH[self.month]
##        if days_in_month == 28 and Date.isLeapYear == True:
##            days_in_month = 29
##        if self.day + 1 <= days_in_month:
##            self.day += 1
##        else:
##            self.day = 1
##            self.month += 1
##        if self.month > 12:
##            self.month = 1
##            self.year += 1

        days_in_month = DAYS_IN_MONTH[self.month]
        if days_in_month == 28 and (self.year % 4 == 0 and not (self.year % 100 == 0 and self.year % 400 != 0)):
            days_in_month = 29
        if self.day + 1 <= days_in_month:
            self.day += 1
        else:
            self.day = 1
            self.month += 1
        if self.month > 12:
            self.month = 1
            self.year += 1
	
    def yesterday(self):
        '''
        Represents one calendar day before the date originally represented
        '''
        days_last_month = DAYS_IN_MONTH[self.month - 1]
        if days_last_month == 28 and (self.year % 4 == 0 and not (self.year % 100 == 0 and self.year % 400 != 0)):
            days_last_month = 29
        if days_last_month == 0:
            days_last_month = DAYS_IN_MONTH[12]
        if self.day - 1 > 0:
            self.day -= 1
        else:
            self.day = days_last_month
            self.month -= 1
        if self.month == 0:
            self.month = 12
            self.year -= 1

    def addNDays(self, N):
        '''
        Changes the calling object so that it represents N calendar days
        after the date originally represented
        '''
        for _ in range(N + 1):
            print(self)
            self.tomorrow()
        self.yesterday()

    def subNDays(self, N):
        '''
        Changes the calling object so that it represents N calendar days 
        before the date originally represented
        '''
        for _ in range(N + 1):
            print(self)
            self.yesterday()
        self.tomorrow()

    def isBefore(self, d2):
        '''
        Returns True if calling object is a calendar date before the input d2.
        If self and d2 represent the same day, return False.
        If self is after d2, return False.
        '''
        if d2.month == self.month and d2.day == self.day and d2.year == self.year:
            return False
        if self.year > d2.year:
            return False
        if self.year == d2.year and self.month > d2.month:
            return False
        if self.year == d2.year and self.month == d2.month and self.day > d2.day:
            return False
        else:
            return True

    def isAfter(self, d2):
        '''
        Returns True if calling object is after the input date d2.
        If self and d2 are the same day, return False.
        If self is before d2, return False.
        '''
        if d2.month == self.month and d2.day == self.day and d2.year == self.year:
            return False
        if self.year < d2.year:
            return False
        if self.year == d2.year and self.month < d2.month:
            return False
        if self.year == d2.year and self.month == d2.month and self.day < d2.day:
            return False
        else:
            return True

    def diff(self, d2):
        '''
        Represents the number of days between self and d2
        '''
        countDays = 0
        day1 = self.copy()
        day2 = d2.copy()
        if self.month == d2.month and self.day == d2.day and self.year == d2.year:
            return 0
        if day1.isBefore(day2):
            while day1.isBefore(day2):
                countDays += 1
                day1.tomorrow()
            countDays *= -1
        else:
            while day1.isAfter(day2):
                countDays += 1
                day1.yesterday()
        return countDays

    def dow(self):
        '''
        Represents the day of the week in a string.
        '''
        dows = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        knownDate = Date(11, 7, 2011)
        diffDays = self.diff(knownDate)
        weekday = diffDays % 7
        return dows[weekday]
