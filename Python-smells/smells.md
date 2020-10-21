# Smells commentary

In suggested order of seriousness.

## No description of purpose

It's initially unclear what this is even supposed to do—one has to infer it. This is exhibited in several aspects of the program:

* The initial "Thirty days…" comment is cryptic and unhelpful
* The method name is minimalist, and unhelpful
* The only test is unhelpful

We'll assume that the design goal of this method is that given a date in day/month/year format via the parameters, this method is supposed to return the "day of the year number" of that date, where January 1st is day 1 of the year, January 2nd is day 2, February 1st is day 32, etc.

## No meaningful tests

Even after conjecturing the purpose, given the grotty nature of the implementation it is hard to know whether this thing works or not. Some more tests would perhaps help us to gain some confidence.

### November doesn't have 31 days!

Adding a trivial test for Dec 31st reveals that there is indeed at least one bug:

``` text
File "./day_of_year.py", line 8, in __main__.dayOfYear
Failed example:
    dayOfYear(12, 31)
Expected:
    365
Got:
    366
```

### No edge case/exception handling

There's no clarity on what the expected behaviour is when nonsensical input is provided.

Perhaps `month` should be restricted to values from 1—12 inclusive, and dayOfMonth constrained to appropriate values for that month (and for February that's dependent on the year—see the note elsewhere about leap year handling!)?

## Implementing something that already exists

The standard Python `datetime` module can do this quite easily, and handles the edge cases sensibly—see `delta.py` for an example (which also has a few more tests). NB this does not handle the Julian/Gregorian transition in 1752—it "[uses an idealized calendar](https://docs.python.org/3/library/calendar.html), the current Gregorian calendar indefinitely extended in both directions". This transition happened at different times in other countries, eg Greece dropped 13 days in 1923, so it's a thorny one to tackle without deep locale support.

## Long `if`/`elif` structure

This is ugly to read, and given a sensible data structure for month lengths should be replaced with a lookup.

### Weird ordering of months

The ordering of the months doesn't follow any natural ordering in the implementation—it's sorted with the shortest months first in the order according to the "mnemonic" in the comment at the top, and then the 31-day months numerically!

## Unused `year` parameter

This is a flaw in and of itself, but it also points to a latent bug: leap years are not handled. It's also unclear why it's the only parameter to have a default, and why that default is 2000.

### Leap years not handled

Note that leap year handling is non-trivial: the basic rules are that it's a leap year every four years, except for "century years", unless the year is divisible by 400—1900 was not a leap year, but 2000 was. There was also a significant disturbance in September 1752 when the Julian calendar replaced the Gregorian one. For more details, refer to [Wikipedia's "Leap year" entry](https://en.wikipedia.org/wiki/Leap_year).

## Parameter treated as variable

The `dayOfMonth` parameter is treated as an accumulator variable within the method.

### Badly named variable

`dayOfMonth` becomes a misleading name when we add the extra "whole month" values to it. This is also a non-conventional name, but that's handled as a separate item elsewhere.

## Magic numbers everywhere

None of the months are given names, just numbers. There is a lot of replication of numbers (month lengths). There are a couple of particularly egregious ones—90 and 59!

## Repetition of numbers; no use of data structures

There are multiple repetitions of the basic facts about the number of days in a given month. This should be held as reference data in a structure. Note that the interface to this is interesting, given that months are one-indexed and Python lists are zero-indexed.

## Inconsistent naming conventions

The program file is called `day_of_year.py`, and the only method is `dayOfYear`—which doesn't follow Python convention. Similarly, `monthOfYear` is not a Pythonic name—[PEP 8 says](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names) "names should be lowercase, with words separated by underscores as necessary to improve readability".

## Parameters in odd order

They are in month / day / year order—the natural order would be to put them in ISO-8601 order, ie most significant bit first: year / month / day. Note that this also matches the native Python convention.
