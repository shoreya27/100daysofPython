# Give no. of days in the given month of given year

year = int(input("Enter a Year: "))
month = int(input("Enter a Month: "))

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def days_in_month(year, month):
    """
    Given the year and Month, this will return how many 
    days are there in that month of the year.
    """

    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

    # check whether year is leap
    is_leap_yr = is_leap(year=year)
    if is_leap_yr and month == 2:
        return 29
    return month_days[month - 1]

print(days_in_month(year=year, month=month))