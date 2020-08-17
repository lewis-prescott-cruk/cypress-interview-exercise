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
* Check that the tests pass cleanly by running them:

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

### Prerequisites

* the candidate will need a GitHub account (VS Code Live Share might work with a Microsoft account, but this is untested)
* they can use the fat VS Code app, or the web client

### Introduction

> We're going to solve a problem together; we would like a bit of Python to generate the Fibonacci sequence. We've got a little skeleton with some tests; let's get an editor going and have a look."

* open the editor
* show the source code; `exercise/__init__.py`
* start live share
  * ⌘⇧P / live share: start collaboration session
  * sign in with Microsoft
  * paste the invite (a `visualstudio.com` URL) into whatever chat you have going with the candidate
  https://prod.liveshare.vsengsaas.visualstudio.com/join?DF6041E8734FBC909D034CE2DD1411A10FC2
  * get them to do Hamburger / View / Terminal
* remember there is the audio option—use the menu on the 🎖 status bar at the bottom of the editor window
* run the tests: `make`

* Hand them the (virtual) keyboard: "GO!"

### The exercise

* write a fibonacci() method; our requirements are:
  * When we pass the function some number n we expect it to return the number that is in position n in the sequence, with the zeroth number being 1.
  * Our function should raise a ValueError if we pass in a number less than 0 because it makes no sense to have anything before the zeroth position in the sequence.

### Wrap-up

* check their work in to the branch `git commit -m "exercise finished" .`
* push the branch to upstream `git push`
* you might like to `make lint` to see what flake8 thinks
