#Accept Directory name from user and delete all duplicate files from the specified directory by
#considering the checksum of files.
#Create one Directory named as Marvellous and inside that directory create log file which
#maintains all names of duplicate files which are deleted.
#Name of that log file contains the date and time at which that file gets created.
#Accept duration in minutes from user and perform task of duplicate file removal after the specific
#time interval.
#Accept Mail id from user and send the attachment of the log file.
#Mail body contains statistics about the operation of duplicate file removal.

#DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com

import os;
import time;
import psutil;
import smtplib;
import chksum;
import schedule;
from sys import *;
from email import encoders;
import urllib.request as urllib2;
from datetime import datetime;
from email.mime.text import MIMEText;
from email.mime.base import MIMEBase;
from email.mime.multipart import MIMEMultipart;

def DelCpy(name, path,mailID):
    flag = os.path.isabs(path);
    if (flag == False):
        path = os.path.abspath(path);

    exists = os.path.isdir(path);
    dups = {};

    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            for filen in fileList:
                path = os.path.join(dirName, filen);
                file_hash = chksum.hashfile(path);
                if file_hash in dups:
                    dups[file_hash].append(path);
                else:
                    dups[file_hash] = [path];
        return printdups(name, dups,mailID);
    else:
        print("Invalid argument or It is not a directory.");


def printdups(name, arr,mailID):
    c = list(os.path.splitext(name));
    log_path = "LogOf" + c[0] + ".txt";
    fobj = open(log_path, "w");
    result = list(filter(lambda x: len(x) > 1, arr.values()));
    if len(result) > 0:
        fobj.write("Duplicates are :\n")
        cnt = 0;
        for r in result:
            for sub in r:
                cnt += 1;
                if cnt >= 2:
                    c = list(os.path.split(sub));
                    fobj.write(c[1] + "\n");
                    os.remove(sub);
            cnt = 0;
    else:
        fobj.write("No Duplicates Found\n")
        
    fobj.close();
        
    connected = is_connected();

    if connected:
        start_time = time.time();
        MailSender(log_path, time.ctime(),mailID);
        end_time = time.time();

        print("The Script took %s time to evaluate." % (end_time - start_time));

    else:
        print("There's no internet connection.");

def is_connected():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=2);
        return True;

    except urllib2.URLError as E:
        return False;


def MailSender(filename, time,mailID):
    try:
        fromaddr = 'kaustubh1khairnar@gmail.com';
        toaddr = mailID;

        msg = MIMEMultipart();
        msg['From'] = fromaddr;
        msg['To'] = toaddr;

        body = """Hello %s,
        
        Please find attached document which contains log file of duplicate files which were removed by the script
        
        LogFile is created at : %s
    
        This is auto generated mail.
    
        Thanks & Regards,
        Kaustubh Khairnar.
        """ % (toaddr, time);

        Subject = """
        DuplicateFileRemoval script generated at : %s
        """ % (time);

        msg['Subject'] = Subject;
        msg.attach(MIMEText(body, 'plain'))
        attachment = open(filename, "rb");
        p = MIMEBase('application', 'octet-stream');
        p.set_payload((attachment).read());
        encoders.encode_base64(p);
        p.add_header('Content-Disposition', "attachment;filename = %s" % filename)
        msg.attach(p);
        s = smtplib.SMTP('smtp.gmail.com', 587);
        s.starttls();
        s.login(fromaddr, "Sonal@08");
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text);
        s.quit();
        print("Log File Successfully sent through mail");

    except Exception as E:
        print("Unable to send email", E)

def main():

    try:
        start_time = time.time();
        schedule.every(int(argv[2])).minutes.do(DelCpy,name=argv[0],path=argv[1],mailID=argv[3]);

        while True :
            schedule.run_pending();
            time.sleep(1)
            
        end_time = time.time();
        
        print("Total time required for execution",(end_time-start_time))
        print("Thank you for using our script");
    except Exception as E:
        print("ERROR :", E);
    


if __name__ == "__main__":
    main();
