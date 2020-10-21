# Thirty days have November, April, June, and September. February has 28 alone,
# and all the rest have 31.
def dayOfYear(month, dayOfMonth, year=2000):
    '''
    >>> dayOfYear(1, 1)
    1

    '''

    if month == 11:
        dayOfMonth += 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
    elif month == 4:
        dayOfMonth += 90
    elif month == 6:
        dayOfMonth += 31 + 28 + 31 + 30 + 31
    elif month == 9:
        dayOfMonth += 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
    elif month == 2:
        dayOfMonth += 31
    elif month == 3:
        dayOfMonth += 59
    elif month == 5:
        dayOfMonth += 31 + 28 + 31 + 30
    elif month == 7:
        dayOfMonth += 31 + 28 + 31 + 30 + 31 + 30
    elif month == 8:
        dayOfMonth += 31 + 28 + 31 + 30 + 31 + 30 + 31
    elif month == 10:
        dayOfMonth += 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30
    elif month == 12:
        dayOfMonth += 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 31

    return dayOfMonth


if __name__ == "__main__":
    import doctest
    doctest.testmod()
