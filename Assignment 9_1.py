#1.Write a program which accepts file name from user and check whether that file exists in
#current directory or not.

import os;
from sys import *;

def solo(path):
    flag = os.path.isabs(path);

    if (flag == False):
        path = os.path.abspath(path);

    exists = os.path.isdir(path);

    if exists:
        print("The File exists in directory");
    else:
        print("There's no such file in directory");


def main():
    if (len(argv) < 2):
        print();
        print("ERROR : Invalid number of arguments entered");
        exit();

    try:
        solo(argv[1]);
    except Exception as E:
        print("ERROR : ", E);


if __name__ == "__main__":
    main();
