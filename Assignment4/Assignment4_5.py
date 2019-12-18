# 5.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
# return Maximum number from that numbers. (You can also use normal functions instead of
# lambda functions).

from functools import *;
from Num import *;


def main():
    value = input("Enter the length of the list ");
    take(int(value));


def take(no):
    arr = list();
    for i in range(no):
        num = input("Enter element : ");
        arr.append(int(num));

    brr = list();
    brr = list(filter(lambda n: (chkprime(n) == True), arr));
    print(brr)

    crr = list(map(lambda x: x * 2, brr))
    print(crr)

    drr=reduce(max,crr)
    print(drr);

if __name__ == "__main__":
    main();
