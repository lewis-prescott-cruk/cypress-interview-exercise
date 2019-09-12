def palindrome(s):
    '''
    Return True for a palindromic string, ie one that reads the same backwards
    as forwards, and False for all other strings.

    >>> palindrome("a")
    True

    >>> palindrome("ab")
    False

    >>> palindrome("abba")
    True

    >>> palindrome("aba")
    True

    >>> palindrome(str.lower("Able was I ere I saw Elba").replace(" ", ""))
    True

    >>> palindrome("bananas")
    False

    '''
    return True


def longestPalindrome(s):
    '''
    Returns the length of the longest palindrome within a string.
    '''
    return 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
