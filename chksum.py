import os;
from sys import *;
import hashlib;

def hashfile(path,blocksize=1024):
    afile = open(path,'rb');
    hasher = hashlib.md5();
    buf = afile.read(blocksize);
    while(len(buf)>0):
        hasher.update(buf);
        buf = afile.read(blocksize);
    afile.close();
    return hasher.hexdigest();
    
def DisplayChkSum(path):
    flag = os.path.isabs(path);
    if not flag:
        path = os.path.abspath(path);
        
    exists = os.path.exists(path);
    
    if exists:
        for dirName,subdirs,fileList in os.walk(path):
            c = list(os.path.split(dirName));
            print("Current Folder :",c[1]);
            for filen in fileList:
                d = list(os.path.split(filen));
                path = os.path.join(dirName,filen);
                file_hash = hashfile(path);
                print("Filename :",d[1]);
                print("ChkSum :",file_hash);
                print('-'*41);
                print();
    else:
        print("Invalid path");
        
def main():
    print();
    print("Designed and Developed by Kaustubh Khairnar");
    print("Application name :",argv[0]);
    
    if (len(argv) != 2):
        print("Invalid Number of arguments");
        exit();
        
    if ((argv[1] == '-h') or (argv[1] == '-H')):
        print("This script is used to traverse the directory and to display checksum of files");
        exit();
        
    if((argv[1] == '-u') or (argv[1] == '-U')):
        print("Usage:");
        print("ApplicationName Path Extension");
        exit();
        
    try : 
        arr = DisplayChkSum(argv[1]);
    
    except ValueError:
        print("ERROR : Invalid datatype of input");
    
    except Exception as E:
        print("ERROR : ",E);
        
if __name__ == "__main__":
    main();
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        