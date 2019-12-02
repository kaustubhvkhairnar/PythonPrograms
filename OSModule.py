import psutil;
import platform;
from os import *;
from datetime import datetime;


def CPU_INFO_OS():
    print("--------CPU_INFO_OS--------");
    if platform.system == 'Windows':
        return platform.processor();
    elif platform.system == 'Darwin':
        command = '/usr/sbin/sysctl -n machdep.cpu.brand_string';
        return popen(command).read().strip();
    elif platform.system == 'Linux':
        command = 'cat/proc/cpuinfo';
        return popen(command).read().strip();
    return 'Platform not identified.';

def get_size(bytes,suffix = "B"):
    factor = 1024;
    for unit in ["","K","M","G","T","P"]:
        if bytes< factor :
            return f"{bytes:.2f}{unit}{suffix}";
        bytes /= factor;

def Platform_Info():
    print("--------SystemInformation--------");
    uname = platform.uname();
    print(f"System : {uname.system}");
    print(f"Nodename : {uname.node}");
    print(f"Release : {uname.release}");
    print(f"Version : {uname.version}");
    print(f"Machine : {uname.machine}");
    print(f"Processor : {uname.processor}");

def Boot_Info():
    print("--------Boot Time--------");
    boot_time_timestamp = psutil.boot_time();
    bt = datetime.fromtimestamp(boot_time_timestamp);
    print(f"Boot Time : {bt.year}/{bt.month}/{bt.day}  {bt.hour} : {bt.minute} : {bt.second}");

def CPU_Info():
    print("------------CPU INFO------------");
    print("Physical Cores : ",psutil.cpu_count(logical=False));
    print("Total Cores : ",psutil.cpu_count(logical=True));

    cpufreq = psutil.cpu_freq();
    print(f"Maximum Frequency : {cpufreq.max:.2f}Mhz");
    print(f"Minimum Frequency : {cpufreq.min:.2f}Mhz");
    print(f"Current Frequency : {cpufreq.current:.2f}Mhz");
    print("CPU Usage Per Core :");
    for i,percentage in enumerate(psutil.cpu_percent(percpu=True)):
        print(f"Core{i} : {percentage}%");
    print(f"Total CPU Usage : {psutil.cpu_percent()}%");

def RAM_Usage():
    print("--------Memory Information--------");
    svmem = psutil.virtual_memory();
    print(f"Total : {get_size(svmem.total)}");
    print(f"Available : {get_size(svmem.available)}");
    print(f"Used : {get_size(svmem.used)}");
    print(f"Percentage : {get_size(svmem.percent)}%");

    print("--------SWAP--------");
    swap = psutil.swap_memory();
    print(f"Total : {get_size(swap.total)}");
    print(f"Free : {get_size(swap.free)}");
    print(f"Used : {get_size(swap.used)}");
    print(f"Percentage : {get_size(swap.percent)}%")

def Disk_Info():
    print("--------Disk Information--------");
    print("Partitions And Usage");
    partitions = psutil.disk_partitions();
    for partition in partitions:
        print(f"=== Device:{partition.device} ===");
        print(f"   Mountpoint : {partition.mountpoint}");
        print(f"   FileSystem Type : {partition.fstype}");
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint);
        except PermissionError:
            continue;

    print(f"   Total Size : {get_size(partition_usage.total)}");
    print(f"   Used : {get_size(partition_usage.used)}");
    print(f"   Free : {get_size(partition_usage.free)}");
    print(f"   Percentage : {get_size(partition_usage.percent)}");

    disk_io = psutil.disk_io_counters()

    print(f"Total read : {get_size(disk_io.read_bytes)}")
    print(f"Total write : {get_size(disk_io.write_bytes)}")
