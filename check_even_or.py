def check_even_or_odd(a):
    if a % 2 == 0:
        return "Even"
    else:
        return "Odd"

# arguments passing or input giving!!
x = int(input("Enter a number: "))

# y = int(input("Enter a number: "))

# call
Output = check_even_or_odd(x)
print(Output)