#3.Write a program which contains filter(), map() and reduce() in it. Python application which
#contains one list of numbers. List contains the numbers which are accepted from user. Filter
#should filter out all such numbers which greater than or equal to 70 and less than or equal to
#90. Map function will increase each number by 10. Reduce will return product of all that
#numbers.

from functools import *;

def main():
    value = input("Enter the length of the list ");
    take(int(value));


def take(no):
    arr = list();
    for i in range(no):
        num = input("Enter element : ");
        arr.append(int(num));
    print(arr);
    brr = list(filter(lambda no : no in range(70,91), arr));
    print(brr);

    crr=list(map(lambda n:n+10,brr))
    print(format(crr));

    drr=reduce(lambda no,no2:no*no2,crr)
    print(drr)

if __name__ == "__main__":
    main();
