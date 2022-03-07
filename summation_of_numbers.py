x = int(input("Enter a number 1: "))
y = int(input("Enter a number 2: "))
z = int(input("Enter a number 3: "))

summation = lambda a, b, c: a + b + c // 3

# summation //= 3

op = summation(x, y, z)

print(op)