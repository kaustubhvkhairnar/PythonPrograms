import sys;
import os;
import schedule;
import time;
import psutil;
from datetime import datetime;

def ProcessDisplay(path):

    if not os.path.exists(path):
        os.mkdir(path);
    
    
    filename = os.path.join(path,"Processlog%s.log"%(datetime.now().strftime("%d_%m_%Y__%H_%M_%S_")));
    
    fobj = open(filename,"w");
    
    line = "-"*70;
    
    fobj.write(line +"\n");
    fobj.write("Process Log at : %s\n"%time.ctime());
    fobj.write(line +"\n");
    
    for pobj in psutil.process_iter():
        fobj.write(str(pobj)+"\n");

    fobj.close()
    

def displayhelp():
	line = "-"*55
	print(line)
	print()
	print("-----------------------USAGE---------------------------")
	print()
	print("python ApplicationName.py FolderName")
	print()
	print("-----------------------EXAMPLE-------------------------")
	print()
	print("python processlogger.py logs")
	print()
	print(line)

def main():
	line = "-"*55
	print(line)
	print()
	print("Process Logger Automation Script")
	print()
	print(line)
	print()
	try:
		schedule.every(1).minute.do(ProcessDisplay,path = sys.argv[1]);
		
		#For Never Ending Loop : use while True
		while True: 
			schedule.run_pending();
			time.sleep(1)
			
	except Exception as E:
		print("ERROR : ",E)
		displayhelp()
		print("Thank you for using our script")
		print(line)
        print()
if __name__ == "__main__":
    main(); 
