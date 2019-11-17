# 5.Design python application which contains two threads named as thread1 and thread2.
# Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on
# screen. After execution of thread1 gets completed then schedule thread2.

import threading;


def dis1():
    for i in range(1, 51):
        print("Display 1-50 : ", i);


def dis2():
    for i in range(50, 0, -1):
        print("Display 50-1 : ", i);


if __name__ == "__main__":
    t1 = threading.Thread(target=dis1, args=());
    t2 = threading.Thread(target=dis2, args=());

    t1.start();
    t1.join();
    t2.start();
    t2.join();
