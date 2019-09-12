# Implement the Fibonacci sequence
fib <- function(n) {
  return(as.integer(n))
}

# Unit tests
library(purrr)
(actual <- (map(1:10, fib) %>% flatten_int()))
(expected <- c(1, 1, 2, 3, 5, 8, 13, 21, 34, 55))
all.equal(actual, expected)
