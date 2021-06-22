## boring class created for mock testing ##
class Calendar:
    def __init__(self):
        ## do nothing
        pass

    def is_weekday(self, date):
        # Python's datetime library treats Monday as 0 and Sunday as 6
        return (0 <= date.day() < 5)

    def is_leap_year(self, date):
        year = date.year()
        if not isinstance(year, int): 
            raise TypeError('not integer')
        if (year % 4) == 0:
           if (year % 100) == 0:
              if (year % 400) == 0:
                 return True
              else:
                 return False
           else:
               return True
        else:
            return False
