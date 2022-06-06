#2. Write a program which accept file name from user and open that file and display the contents
#of that file on screen.

import os;
from sys import *;

def read(file):
    exists = os.path.exists(file);
    if exists:
        fobj = open(file,"r");
        print(fobj.read());
    else :
        print("No such File in directory");
def main():
    try:
        read(argv[1]);
    except Exception as E:
        print("ERROR : ",E);

if __name__ == "__main__":
    main();
