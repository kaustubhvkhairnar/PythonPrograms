# 3.Design python application which creates two threads as evenlist and oddlist. Both the
# threads accept list of integers as parameter. Evenlist thread add all even elements
# from input list and display the addition. Oddlist thread add all odd elements from input
# list and display the addition.
from functools import *;
import threading;

def Evenlist(arr):
    brr = list(filter(lambda n: (n % 2 == 0), arr));
    crr = reduce(lambda x, y: x + y, brr)
    print("Evenlist Addition : ", crr)


def Oddlist(arr):
    brr = list(filter(lambda n: (n % 2 != 0), arr));
    crr = reduce(lambda x, y: x + y, brr)
    print("Oddlist Addition: ", crr)


if __name__ == "__main__":
    no = int(input("Enter number of elements in list : "))
    arr = list();
    for i in range(no):
        num = int(input("Enter number : "))
        arr.append(num);

    print("Entered list is : ", arr);

    t1 = threading.Thread(target=Evenlist, args=(arr,));
    t2 = threading.Thread(target=Oddlist, args=(arr,));

    t1.start();
    t2.start();

    t1.join();
    t2.join();
