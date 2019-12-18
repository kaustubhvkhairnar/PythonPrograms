#5.Write a program which accept N numbers from user and store it into List. Return addition of all
#prime numbers from that List. Main python file accepts N numbers from user and pass each
#number to ChkPrime() function which is part of our user defined module named as
#MarvellousNum. Name of the function from main python file should be ListPrime().

from Num import *;


def main():
    num = int(input("Enter number of elements : "))
    listprime(num);


def listprime(no):
    print("Enter", no, "Element/s");
    arr = [];
    for i in range(no):
        print("Enter", i + 1, "element");
        num = int(input());
        arr.append(num);

    sum = 0;

    for i in range(no):
        if (chkprime(arr[i]) == True):
            sum = sum + arr[i];
            print("Prime number is i :",i,"arr[]:",arr[i]);

    print("Given elements : ", arr);
    print("Sum of prime numbers is : ", sum);


if __name__ == "__main__":
    main();
