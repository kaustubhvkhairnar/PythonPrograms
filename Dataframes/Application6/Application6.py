import os
import xlsxwriter
import fnmatch
from sys import *

def ExcelCreate(name):
    workbook = xlsxwriter.Workbook(name)
    worksheet = workbook.add_worksheet()
    
    worksheet.write('A1','Name')
    worksheet.write('B1','College')
    worksheet.write('C1','MailID')
    worksheet.write('D1','Phone')
    
    workbook.close()
    
def main():
    
    print("Applicarion Name :",argv[0])
    
    if(len(argv)!=2):
        print()
        print("Invaild number of arguments")
        print()
        print("Type -h for help")
        print()        
        print("Type -u for usage")
        exit()
        
    if(argv[1] == '-h') or  (argv[1] == '-H'):
        print("The script is used to create excel file and write data into it")
        exit()
        
    if(argv[1] == '-u') or  (argv[1] == '-U'):
        print("Usage : Application_Name.py Name_of_File")
        exit()
        
    try:
        if(argv[1].endswith(".xlsx")):
            ExcelCreate(argv[1])
        else:
            argv[1] = argv[1]+".xlsx"
            ExcelCreate(argv[1])
    except Exception as E:
        print("Error :",E)
    
if __name__ == "__main__":
    main()
    