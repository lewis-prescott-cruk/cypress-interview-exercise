# Python exercise

## Prequisites

* make sure you have Python 3 and that you're using it. If in doubt, install a virtual environment locally like this:
  * [install `pyenv`](https://github.com/pyenv/pyenv#installation)
    * on a Mac with Homebrew, `brew bundle install --file=Brewfile`
  * `pyenv install 3.7.4` (you can check that this is still the latest stable version  with `pyenv install --list`)
* `make`(1)
* install `pipenv` (the Brewfile will do this on a Mac)
* make sure you have a sensible Python editor; VS Code recommended, or PyCharm if you have a license for it

## Setup

Do this ahead of the interview, in case it doesn't go 100% smoothly!

* Clone the repo: `git clone https://github.com/CRUKorg/interview-exercises.git`
* set up a local Python environment in your working directory:
  * `pyenv local 3.7.4` — this should be the latest stable version of Python 3; see prerequisites above
  * `pipenv sync` — this will install any extra Python modules required into your virtualenv
* Make a new branch for the interviewee to work in: `git checkout -b <Workday Candidate ID>`
* Open `example/__init__.py` in the editor
* Check that the unit tests pass cleanly by running them:

``` shellsession
➭ make
pipenv run python3 -m unittest discover --verbose --start-directory tests/
test_palindrome (test_palindrome.Test) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

## Interview procedure

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
