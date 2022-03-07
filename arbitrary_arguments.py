def names(*name):  # instead of passing all the values or arguments as well.
    return name[0]
x = "Sameer"
y = "Dhanush"
z = "Pradeep"


op = names(x, y, z) # not to pass *name in that.
print(op)
