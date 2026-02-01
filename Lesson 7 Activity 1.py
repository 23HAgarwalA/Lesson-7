x = 32
if (type(x) is float):
    print (x, "is a value with a decimal number")
else:
    print (x, "is an integer")

y = 1.423413
if (type(y) is not int):
    print (y, "is not an integer")
else:
    print (y, "is an integer")

a = 98
b = 97
if (x is not y):
    print (x, "and", y, "don't have the same value")
else:
    print (x, "and", y, "are the same")

a = ("fgh")
b = ("fgh")
if (a is b):
    print (a, "and", b, "are the same")
else:
    print (a, "and", b, "aren't the same")
