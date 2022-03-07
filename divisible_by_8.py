def check_even_or_odd(a):
    if a % 8 == 0:
        return "Divisible by 8"
    else:
        return "Not divisible by 8"

# arguments passing or input giving!!
x = int(input("Enter a number: "))

# call
Op = check_even_or_odd(x)
print(Op)