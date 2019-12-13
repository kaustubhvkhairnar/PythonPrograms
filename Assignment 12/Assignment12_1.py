#1.Design automation script which display information of running processes as its name, PID, Username.

import psutil;


def ProcessDisplay():
    listpro = [];

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username']);
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024);
            listpro.append(pinfo);

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass;

    return listpro;


def main():
    listpro = ProcessDisplay();

    for j in listpro:
        print(j);


if __name__ == "__main__":
    main();
