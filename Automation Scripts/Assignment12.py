#12. Design automation script which accept directory name and mail id from user and create log
#file in that directory which contains information of running processes as its name, PID,
#Username. After creating log file send that log file to the specified mail.

# Automation script which sends text and attachment Email through the python script.

import os;
import time;
import psutil;
import smtplib;
from datetime import datetime;
import schedule;
from sys import *;
from email import encoders;
import urllib.request as urllib2;
from email.mime.text import MIMEText;
from email.mime.base import MIMEBase;
from email.mime.multipart import MIMEMultipart;


def is_connected():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=2);
        return True;

    except urllib2.URLError as E:
        return False;


def MailSender(filename, time,mailID):
    try:
        fromaddr = """Senders MailID""";
        toaddr = mailID;

        msg = MIMEMultipart();
        msg['From'] = fromaddr;
        msg['To'] = toaddr;

        body = """Hello %s,
    Please find attached document which contains log file of running processes
        
    LogFile is created at : %s
    
    This is auto generated mail.
    
    Thanks & Regards,
    Kaustubh Khairnar
        """ % (toaddr, time);

        Subject = """
        ProcessLog generated at : %s
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
        s.login(fromaddr,  """Password of sender""");
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text);
        s.quit();
        print("Log File Successfully sent through mail");

    except Exception as E:
        print("Unable to send email", E)


def ProcessLog(log_dir,mailID):
    listpro = [];

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir);
        except:
            pass;

    line = "-" * 55;

    log_path = os.path.join(log_dir, "Processlog%s.log" %(datetime.now().strftime("%d_%m_%Y %H_%M_%S")));
    str(log_path)
    fobj = open(log_path, "w");

    fobj.write(line + "\n");
    fobj.write("Process Logger at : %s\n" % time.ctime());
    fobj.write(line + "\n");
    fobj.write("\n");

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username']);
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024);
            listpro.append(pinfo);

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass;

    for element in listpro:
        fobj.write("%s\n" % element);

    print("Log file successfully generated at location %s" % (log_path));

    connected = is_connected();

    if connected:
        start_time = time.time();
        MailSender(log_path, time.ctime(),mailID);
        end_time = time.time();

        print("The Script took %s time to evaluate." % (end_time - start_time));

    else:
        print("There's no internet connection.");


def main():
    try:
        schedule.every(1).minutes.do(ProcessLog,log_dir = argv[1],mailID = argv[2]);
        while True:
            schedule.run_pending();
            time.sleep(1);

    except ValueError:
        print("Invalid datatype of input");

    except Exception as E:
        print(E)


if __name__ == "__main__":
    main()
