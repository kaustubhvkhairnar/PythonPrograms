# 6. Design automation script which accept directory name and two file extensions from user.
# Rename all files with first file extension with the second file extention.


import os;
from sys import *;


def DirectoryRename(path, ext, ext2):
    flag = os.path.isabs(path);
    if (flag == False):
        path = os.path.abspath(path);

    exists = os.path.isdir(path);

    if exists:
        print();

        for Folder, Subfolders, Files in os.walk(path):
            c = list(os.path.split(Folder));
            print ("Folder Name :", c[1]);
            for fi in Files:
                newfile = os.path.join(Folder, fi);
                if newfile.endswith(ext):
                    pre, ext = os.path.splitext(newfile)
                    os.rename(newfile, pre + ext2)
                    d = list(os.path.split(pre));
                    print ("Changed File Name :", d[1] + ext2);
                elif fi.endswith(ext2):
                    print("File Name :", fi);
    else:
        print();
        print("ERROR : Invalid path or There's no such directory");


def main():
    try:
        DirectoryRename(argv[1], argv[2], argv[3]);
    except Exception as E:
        print("ERROR ", E);

    print("Thank you for using our script");


if __name__ == "__main__":
    main();
