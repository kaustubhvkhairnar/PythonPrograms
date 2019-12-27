# 3. Design automation script which accept directory name from user and create log file in that
# directory which contains information of running processes as its name, PID, Username.

import sys;
import os;
import schedule;
import time;
import psutil;
from datetime import datetime;


def ProcessDisplay(path):
    if not os.path.exists(path):
        os.mkdir(path);

    filename = os.path.join(path, "Processlog%s.log" % (datetime.now().strftime("%d_%m_%Y__%H_%M_%S_")));

    fobj = open(filename, "w");

    line = "-" * 55;

    fobj.write(line + "\n");
    fobj.write("Marvellous Process Logger at : %s\n" % time.ctime());
    fobj.write(line + "\n");

    for pobj in psutil.process_iter():
        fobj.write(str(pobj) + "\n");

    fobj.close();


def main():
    ProcessDisplay(sys.argv[1]);

if __name__ == "__main__":
    main();
