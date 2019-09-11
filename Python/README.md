# Python exercise

_TBD_

## Prequisites

* make sure you have Python 3 and that you're using it. If in doubt, install a virtual environment locally like this:
  * [install `pyenv`](https://github.com/pyenv/pyenv#installation)
    * on a Mac with Homebrew, `brew bundle install --file=Brewfile`
  * `pyenv install 3.7.4` (you can check that this is still the latest stable version  with `pyenv install --list`)
  * `pyenv local 3.7.4`
* `make`(1)


## Setup

Do this ahead of the interview, in case it doesn't go 100% smoothly!

* Clone the repo: `git clone https://github.com/CRUKorg/interview-exercises.git`
* Make a new branch for the interviewee to work in: `git checkout -b <Workday Candidate ID>`
* Check that the tests pass cleanly by running them:

``` shellsession
➭ make
python3 -m unittest discover -s tests/
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

## Interview procedure

### Introduction

* show the source code
* run the tests

### The exercise

_TBD_

### Wrap-up

* check their work in to the branch `git add . && git commit -m "exercise finished"`
* push the branch to upstream `git push`
