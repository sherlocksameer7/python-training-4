def smallest_numbers(a, b, c):
    # sort_small = sorted(smallest_numbers[0])
    # return sort_small
    if a < b:
        if a < c:
            return a
    elif b < a and b < c:     # this is only for finding the integers of among the smallest
        return b              # not for string finding
    else:
        return c

x = int(input("Enter a number 1: "))
y = int(input("Enter a number 2: "))
z = int(input("Enter a number 3: "))

smallestNumbers_functions = smallest_numbers(x, y, z)
print(smallestNumbers_functions)
