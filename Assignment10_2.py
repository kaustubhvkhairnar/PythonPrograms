import os;
from sys import *;

def extensionchange(path,ext):
    flag = os.path.isabs(path);
    if (flag == False):
        path = os.path.abspath(path);
        
    exists = os.path.isdir(path);
    
    if exists:
        print();
        for Folder,Subfolder,File in os.walk(path):
            for fi in File:
                if(fi.endswith(ext)):
                    print("Filename is",fi);
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
