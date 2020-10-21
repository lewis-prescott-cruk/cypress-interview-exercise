from datetime import date

def dayOfYear(month, day, year=2000):
    '''Return the day of the year, counting from January 1st as 1, January 2nd as 2
etc. Rejects invalid dates by raising ValueError exceptions.

    >>> dayOfYear(13, -1)
    Traceback (most recent call last):
        ...
    ValueError: month must be in 1..12

    >>> dayOfYear(1, 1, 1970)
    1

    >>> dayOfYear(2, 29, 1970)  # 1970 was not a leap year
    Traceback (most recent call last):
        ...
    ValueError: day is out of range for month

    >>> dayOfYear(12, 31, 2000) # 2000 was a leap year
    366

    >>> dayOfYear(12, 31, 2100) # 2100 will not be a leap year
    365
    '''

    last = date(year, month, day)
    first = date(year, 1, 1)

    delta = last - first

    return(delta.days + 1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
