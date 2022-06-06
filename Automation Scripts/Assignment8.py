#8. Design automation script which accept two directory names and one file extension. Copy all
#files with the specified extension from first directory into second directory. Second directory
#should be created at run time.

import os;
from sys import *;
import shutil;


def CopyFileS(path, dst,ext):
    flag = os.path.isabs(path) and os.path.isabs(dst);
    if (flag == False):
        path = os.path.abspath(path);
        dst = os.path.abspath(dst)

    exists = os.path.isdir(path);
    exists2 = os.path.isdir(dst);

    if not exists2:
        os.mkdir(dst);

    if exists:
        cnt=0;
        for Folder, Subfolders, Files in os.walk(path):
            for Fil in Files:
                if (Fil.endswith(ext)):
                    cnt += 1;
                    newfile = os.path.join(Folder, Fil);
                    shutil.copy(newfile, dst);
                    shutil.copystat(newfile, dst);
        if (cnt == 0):
            print("No such file found with extension :", ext)
    else:
        print();
        print("ERROR : Invalid path or There's no such file in directory");


def main():
    try:
        CopyFileS(argv[1], argv[2],argv[3]);
    except Exception as E:
        print("ERROR ", E);
    print("Thank you for using our script");

if __name__ == "__main__":
    main();
