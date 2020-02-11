
#4.Write a program which accept two file names from user and compare contents of both the
#files. If both the files contains same contents then display success otherwise display failure.
#Accept names of both the files from command line.

import os;
from sys import *;
from termcolor import colored, cprint

def read(file1,file2):
    if ((os.path.exists(file1)) and (os.path.exists(file2))):
        fobj = open(file1, "r");
        nobj = open(file2, "r");
        if(fobj.read() == nobj.read()):
            print(colored('            Success              ','red','on_yellow'))
            print()
        else:
            print(colored('           Failure              ','red','on_yellow'))
            print()
        nobj.close();
        fobj.close();
    else:
        print("No such File in directory")
        #displayhelp()

'''        
def displayhelp():
	line = '-'*43
	cprint("\n------------------",'yellow',end=' ')
	print("HELP",end=' ')
	cprint("------------------\n",'yellow')
	print("This Script is used to check whether the contents of First file and Second file are same or not.")
	print("The script displays 'Success' when the files are same and 'Failure' when not.\n")
	cprint(line,'yellow')
	cprint("\n-----------------",'yellow',end=' ')
	print("USAGE",end=' ')
	cprint("------------------\n",'yellow')
	print("python ApplicationName.py FirstFileName SecondFileName\n")
	cprint(line,'yellow')
	cprint("\n----------------",'yellow',end=' ')
	print("EXAMPLE",end=' ')
	cprint("------------------\n",'yellow')
	print("python DuplicateContents.py hello.txt demo.txt\n")
	cprint(line,'yellow')	
	print()
'''	

def main():
	line = '-'*43
	print()
	cprint(line,'blue')
	print(colored('Designed and Developed by Kaustubh Khairnar', 'yellow', 'on_blue')) 
	cprint(line,'blue')
	print()
	
	try:
		read(argv[1],argv[2])
		
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
