# 5. Accept file name and one string from user and return the frequency of that string from file.

import os;
from sys import *;


def read(file, str):
    cnt = 0;
    if os.path.exists(file):
        fobj = open(file, "r");
        zip = list(fobj.read().split(" "))
        for i in range(len(zip)):
            if (zip[i] == str):
                cnt = cnt + 1;
        print("Count", cnt);


def main():
    try:
        read(argv[1], argv[2]);
    except Exception as E:
        print("Error", E);


if __name__ == "__main__":
    main();
