#4.Write a program which accept two file names from user and compare contents of both the
#files. If both the files contains same contents then display success otherwise display failure.
#Accept names of both the files from command line.

import os;
from sys import *;


def read(file1,file2):
    if ((os.path.exists(file1)) and (os.path.exists(file2))):
        fobj = open(file1, "r");
        nobj = open(file2, "r");
        if(fobj.read() == nobj.read()):
            print("Success");
        else:
            print("Failure")
        nobj.close();
        fobj.close();
    else:
        print("No such File in directory");


def main():
    try:
        read(argv[1],argv[2]);
    except Exception as E:
        print("Error",E);


if __name__ == "__main__":
    main();
