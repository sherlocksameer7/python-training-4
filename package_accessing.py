import calculator_package as calp  # importing the another package to creating with alias name called CALP,
                                   # that can be used for accessing it in definition call by another package using,
                                   # calp.add_numbers().
x = int(input("Enter any number 1: "))
y = int(input("Enter any number 2: "))
op_1 = calp.add_numbers(x, y)
op_2 = calp.sub_numbers(x, y)  # we can access many functions in that importing concept in the packages!!!
op_3 = calp.mul_numbers(x, y)
print(op_1)
print(op_2)
print(op_3)