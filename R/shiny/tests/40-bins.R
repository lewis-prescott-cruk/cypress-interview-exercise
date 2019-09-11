app <- ShinyDriver$new("../")
app$snapshotInit("40-bins")

app$setInputs(bins = 35)
app$setInputs(bins = 40)
app$snapshot()
