# 3.Write a program which accept file name from user and create new file named as Demo.txt and
# copy all contents from existing file into new file. Accept file name through command line
# arguments.

import os;
from sys import *;
from termcolor import colored, cprint 
from colorama import Fore
def read(file):
    exists = os.path.exists(file);
    if exists:
        fobj = open(file, "r");
        nobj = open("Demo.txt", "a")
        nobj.write(fobj.read());
        nobj.close();
        fobj.close();
        print()
        print("Your data is successfully copied from '" + file + "' to 'Demo.txt'\n")
    else:
        print("No such File in directory");
        print()
        #displayhelp()
        
 '''       
def displayhelp():
	line = '-'*43
	cprint("\n------------------",'yellow',end=' ')
	print("HELP",end=' ')
	cprint("------------------\n",'yellow')
	print("This Script is used to copy the contents of one file into another file.\n")
	cprint(line,'yellow')
	cprint("\n-----------------",'yellow',end=' ')
	print("USAGE",end=' ')
	cprint("------------------\n",'yellow')
	print("python ApplicationName.py Filename.extension\n")
	cprint(line,'yellow')
	cprint("\n----------------",'yellow',end=' ')
	print("EXAMPLE",end=' ')
	cprint("------------------\n",'yellow')
	print("python CopyContents.py hello.py\n")
	cprint(line,'yellow')	
	print()
'''	
def main():
	line = '-'*43
	print()
	cprint(line,'blue')
	print(colored('Designed and Developed by Kaustubh Khairnar', 'yellow', 'on_blue')) 
	cprint(line,'blue')
	
	try:
		read(argv[1])
		
	except Exception as E:
		#displayhelp()
		print(colored('ERROR :','yellow','on_red')+colored(E,'yellow','on_red'))
		print()
	line = '-'*30
	cprint(line,'green')
	cprint("Thank you for using our script",'green')
	cprint(line,'green')
	print()
	
if __name__ == "__main__":
    main()
