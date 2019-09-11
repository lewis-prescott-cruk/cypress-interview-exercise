# R interview exercise

## Prerequisites

* Git client
* [R Studio](https://www.rstudio.com/products/rstudio/download/#download)
  * on a Mac with [Homebrew](https://brew.sh) installed: `brew bundle install --file=Brewfile`
* GitHub credentials; use these to locally clone a copy of this repository: `git clone https://github.com/CRUKorg/interview-exercises.git`

Setup instructions; NB you will require an internet connection, and in case it doesn't work entirely smoothly it would be best to do this at your leisure, ie before you are in front of the interviewee!

* Check this repo out
* Make a new branch for the interviewee to work in: `git checkout -b <Workday Candidate ID>`
* Open this project in R Studio
  * from a Mac Terminal.app in this directory, `open R.Rproj`
* Use the R console to install the test framework, including [PhantomJS](http://phantomjs.org/):

``` R
library("devtools")
install_github("rstudio/shinytest")
# If you have plenty of time, you may wish to update all the CRAN packages
# when prompted, but this is not necessary.
library(shinytest)
shinytest::installDependencies()
```

## The exercise

### Introduction

* Ask the interviewee to run the app:
  * find and open `shiny/app.R`
  * click the "▶ Run App" button
* Show how to run the [shinytest](https://rstudio.github.io/shinytest/articles/shinytest.html) tests
  * from the console:

``` R
    library("shinytest")
    testApp("shiny")`
```

* Show how to run unit tests _TBD_

## The exercise

_TBD_

* Find something broken in the app
* Write a test to set expectations
* Fix the problem
* See that the test passes

## Wrap-up

* check their work in to the branch `git add . && git commit -m "exercise finished"`
* push the branch to upstream `git push`
