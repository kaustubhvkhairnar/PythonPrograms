# 3. Design automation script which accept two directory names. Copy all files from first directory
# into second directory. Second directory should be created at run time.

import os;
from sys import *;
import shutil;


def CopyFile(path, dst):
    flag = os.path.isabs(path) and os.path.isabs(dst);
    if (flag == False):
        path = os.path.abspath(path);
        dst = os.path.abspath(dst)

    exists = os.path.isdir(path);
    exists2 = os.path.isdir(dst);

    if not exists2:
        os.mkdir(dst);

    if exists:
        for Folder, Subfolders, Files in os.walk(path):
            c = list(os.path.split(Folder));
            print ("Folder name :", c[1]);
            for Fil in Files:
                newfile = os.path.join(Folder, Fil);
                print("DST", dst);
                print ("File :", Fil);
                shutil.copy(newfile, dst);
                shutil.copystat(newfile, dst);
    else:
        print();
        print("ERROR : Invalid path or There's no such file in directory");


def main():
    try:
        CopyFile(argv[1], argv[2]);
    except Exception as E:
        print("ERROR ", E);
    print("Thank you for using our script");

if __name__ == "__main__":
    main();
