# 3.Write a program which accept file name from user and create new file named as Demo.txt and
# copy all contents from existing file into new file. Accept file name through command line
# arguments.

import os;
from sys import *;


def read(file):
    exists = os.path.exists(file);
    if exists:
        fobj = open(file, "r");
        nobj = open("Demo.txt", "a")
        nobj.write(fobj.read());
        nobj.close();
        fobj.close();
    else:
        print("No such File in directory");


def main():
    try:
        read(argv[1]);
    except Exception as E:
        print("Error",E);


if __name__ == "__main__":
    main();
