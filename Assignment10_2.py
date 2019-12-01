import os;
from sys import *;

def extensionchange(path,ext):
    flag = os.path.isabs(path);
    if (flag == False):
        path = os.path.abspath(path);
        
    exists = os.path.isdir(path);
    
    if exists:
        print();
        max = 0;
        for Folder,Subfolder,File in os.walk(path):
            for fi in File:
                print(fi);
                newpath = Folder + "\" + name;
                print(os.path.getsize(newpath));
                print();
    else:
        print();
        print("ERROR : Invalid path or There's no such file in directory");

def main():
    try:
        extensionchange(argv[1],argv[2]);
    except Exception as E:
        print("ERROR :",E);

if __name__ == "__main__":
    main();
