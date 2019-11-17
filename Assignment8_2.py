# 2.Design python application which creates two threads as evenfactor and oddfactor.
# Both the thread accept one parameter as integer. Evenfactor thread will display
# addition of even factors of given number and oddfactor will display addition of odd
# factors of given number. After execution of both the thread gets completed main
# thread should display message as “exit from main”

import threading;


def evenfactor(no):
    s = 0;
    for i in range(1, no):
        if ((no % i) == 0):
            if ((i % 2) == 0):
                s = s + i;
    print("EvenFactors's sum : ", s);


def oddfactor(no):
    s = 0;
    for i in range(1, no):
        if ((no % i) == 0):
            if (i % 2 != 0):
                s = s + i;
    print("OddFactors's sum : ", s);


if __name__ == "__main__":
    num = 20;
    t1 = threading.Thread(target=evenfactor, args=(num,));
    t2 = threading.Thread(target=oddfactor, args=(num,));

    t1.start();
    t1.join();

    t2.start();
    t2.join();

    print("Exit From Main...")
