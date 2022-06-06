#4. Design automation script which accept directory name and delete all duplicate files from that
#directory. Write names of duplicate files from that directory into log file named as Log.txt.
#Log.txt file should be created into current directory. Display execution time required for the
#script.

import chksum
import os
from sys import *
import time


def DelCpy(name, path):
    flag = os.path.isabs(path)
    if (flag == False):
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    dups = {}

    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = chksum.hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return printdups(name, dups)
    else:
        print("Invalid argument or It is not a directory.")


def printdups(name, arr):
    c = list(os.path.splitext(name))
    fobj = open("LogOf" + c[0] + ".txt", "w")
    result = list(filter(lambda x: len(x) > 1, arr.values()))
    if len(result) > 0:
        fobj.write("Duplicates are :\n")
        print ("Duplicates Found")
        print("Following files are identical")
        cnt = 0
        for r in result:
            for sub in r:
                cnt += 1
                if cnt >= 2:
                    c = list(os.path.split(sub))
                    print (c[1])
                    fobj.write(c[1] + "\n")
                    os.remove(sub)
            cnt = 0
    else:
        fobj.write("No Duplicates Found\n")
        print("No Duplicates Found")


def main():
    try:
        start_time = time.time()
        DelCpy(argv[0], argv[1])
        end_time = time.time()
    except Exception as E:
        print("ERROR :", E)
    print("Total time required for execution",(end_time-start_time))
    print("Thank you for using our script")


if __name__ == "__main__":
    main()
