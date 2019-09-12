# Implement the Fibonacci sequence
fib <- function(n) {
  return(as.integer(n))
}

# Unit tests
# NB if you see "Error: Can't coerce element [n] from a double to a integer"
# then coerce your return value to an integer: return(as.integer(n))
library(purrr)
(actual <- (map(1:10, fib) %>% flatten_int()))
(expected <- c(1, 1, 2, 3, 5, 8, 13, 21, 34, 55))
all.equal(actual, expected)
