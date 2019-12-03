# 1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
# for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
# parameters as number and perform the operation. Write on python program which call all the
# functions from Arithmetic module by accepting the parameters from user.

from Arithmetic import *

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

if __name__ == "__main__":
    Add(num1, num2)
    Sub(num1, num2)
    Mult(num1, num2)
    Div(num1, num2)
