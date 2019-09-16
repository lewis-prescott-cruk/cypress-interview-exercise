# return the nth element of the Fibonacci sequence
fib <- function(n) {
  return(n)
}

# Unit tests
(actual <- sapply(1:10, fib))
(expected <- c(1, 1, 2, 3, 5, 8, 13, 21, 34, 55))
all.equal(actual, expected)
