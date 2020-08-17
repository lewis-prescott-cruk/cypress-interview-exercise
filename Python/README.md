# Python exercise

## Prequisites

* make sure you have Python 3 and that you're using it
* `make`(1)
* make sure you have a sensible Python editor; VS Code recommended, or PyCharm if you have a license for it

## Setup

Do this ahead of the interview, in case it doesn't go 100% smoothly!

* Clone the repo: `git clone https://github.com/CRUKorg/interview-exercises.git`
* Make a new branch for the interviewee to work in: `git checkout -b <Workday Candidate ID>`
* Open `example/__init__.py` in the editor
* Check that the unit tests pass cleanly by running them:

``` shellsession
➭ make test
python3 -m unittest discover --verbose --start-directory tests/
test_palindrome (test_palindrome.Test) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

## Interview procedure

### Standard mandatory questions

A great deal of cancer research is carried out without using animals but in certain areas it’s still necessary if we are to understand, prevent and cure cancer. CRUK only uses animals when there is no alternative. Does this cause you any problems?

Cancer Research UK operates a strict Non Smoking policy – would you have any issues adhering to this?

Do you have any restrictions on your right to work in the UK?

### Introduction

> We're going to solve a problem together; we would like a bit of Python to
detect palindromic strings, ones that read the same forwards as backwards. If we
have time, we'll carry on and write a method to find the length of the longest
palindrome substring. We've got a little skeleton with some tests; let's have a
look."

* open the editor
* show the source code; `exercise/__init__.py`
* run the tests: `make`

* Hand them the keyboard: "GO!"

### The exercise

* write a palindrome() method
* write a longestPalindrome() method
  * uncomment the stub and associated doctests in the exercise module to begin
  * remove the skip annotation from the unit tests in `test/`

### Wrap-up

* check their work in to the branch `git commit -m "exercise finished" .`
* push the branch to upstream `git push`
* you might like to `make lint` to see what flake8 thinks
