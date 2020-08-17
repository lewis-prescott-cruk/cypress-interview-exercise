def fibonacci(n):
    '''
Return the nth number in the Fibonnaci sequence. The Fibonacci sequence
begins as follows:

    1, 1, 2, 3, 5, 8, 13, 21, ...
    0  1  2  3  4  5  6   7       ← 0-indexed sequence

where we start with the numbers 1, 1 and then get the next number in the
sequence by adding the two previous numbers together. For example, the next
number in our example after 21 would be 13 + 21 = 34.

    >>> fibonacci(5)
    8
    '''

    return n


if __name__ == "__main__":
    import doctest
    doctest.testmod()
