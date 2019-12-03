# 1.Design automation script which accept directory name and display checksum of all files.

import chksum;
import os;
from sys import *;


def ChkSum(path):
    exists = os.path.isdir(path);

    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            c = list(os.path.split(dirName));
            print("Current Folder :", c[1]);
            for filen in fileList:
                d = list(os.path.split(filen));
                path = os.path.join(dirName, filen);
                file_hash = chksum.hashfile(path);
                print("Filename :", d[1]);
                print("ChkSum :", file_hash);
                print('-' * 41);
                print();
    else:
        print("Invalid argument or It is not a directory.");


def main():
    try:
        ChkSum(argv[1]);
    except Exception as E:
        print("ERROR :", E);
    print("Thank you for using our script");


if __name__ == "__main__":
    main();
