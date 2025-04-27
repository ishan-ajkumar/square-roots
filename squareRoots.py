import sys
from decimal import Decimal,getcontext
import timeit

getcontext().prec = 102


def isNumber(number):
    for char in number:
        if  not (char == "0" or char == "1" or char == "2"  or char == "3"  or char == "4"  or char == "5"  or char == "6"  or char == "7"  or char == "8"  or char == "9"  or char == "."):
            return False

    if number.count(".") > 1:
        return False

    return True


def babylonianSquareRootMethod(x, a):
    result = (a+(x/a))/2
    return result


def babylonianSquareRootMethod():
    a = 1 
    for _ in range(1,20):
        a = babylonianSquareRootMethod(number, a)
    print(f"Square root of {number} = {a}")


number = input("Please enter a number to take the square root of: ")
if not isNumber(number):
    print("ERROR: Only numbers are allowed")
    sys.exit(1)
else:
    number = Decimal(number)

timeTaken = timeit.timeit(babylonianSquareRootMethod, number=1)
print(f"Time taken: {timeTaken} seconds")
