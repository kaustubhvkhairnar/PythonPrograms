#2.Design automation script which accept process name and display information of that process if it is running.

import psutil;
import sys;

def ProcessDisplay(process):
    listpro = [];

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username']);
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024);
            if pinfo['name'] == process:
                listpro.append(pinfo);
            
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            print ("No Such Running Process");

    return listpro;


def main():
    listpro = ProcessDisplay(sys.argv[1]);

    for j in listpro:
        print(j);


if __name__ == "__main__":
    main();
