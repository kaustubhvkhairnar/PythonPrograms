# 3.Write a program which accept file name from user and create new file named as Demo.txt and
# copy all contents from existing file into new file. Accept file name through command line
# arguments.

import os;
from sys import *;


def read(file):
    exists = os.path.exists(file);
    if exists:
        fobj = open(file, "r");
        nobj = open("Demo.txt", "a")
        nobj.write(fobj.read());
        nobj.close();
        fobj.close();
        print()
        print("Your data is successfully copied from '" + file + "' to 'Demo.txt'")
    else:
        print("No such File in directory");
        print()
        print("------------------USAGE------------------")
        print("python Application.py Filename.extension")
        print("------------------------------------------")	
        
    

def main():
    read(argv[1]);    
	
    print()
    print("Thank you for using our script")
    print()

if __name__ == "__main__":
    main()
