# 4.Design python application which creates three threads as small, capital, digits. All the
# threads accepts string as parameter. Small thread display number of small characters,
# capital thread display number of capital characters and digits thread display number of
# digits. Display id and name of each thread.
import threading;
import os;

def Small(str):
    print("Small PID : ",os.getpid());
    s = 0;
    for i in range(len(str)):
        if (ord(str[i]) >= 97) and (ord(str[i]) <= 122):
            s = s + 1;
    print("Number of small characters in String: ",s);

def Capital(str):
    print("Capital PID : ", os.getpid());
    s=0;
    for i in range(len(str)):
        if (ord(str[i]) >= 65) and (ord(str[i]) <= 90):
            s = s + 1;
    print("Number of Capital characters in String : ",s);

def Digits(str):
    print("Digit PID : ", os.getpid());
    s=0;
    for i in range(len(str)):
        if (ord(str[i]) >= 48) and (ord(str[i]) <= 57):
            s = s + 1;
    print("Number of Digits in String : ", s);

if __name__ == "__main__":
    print("Main PID : ", os.getpid());
    stringi = list(input("Enter any string : "))
    t1 = threading.Thread(target=Small, args=(stringi,));
    t2 = threading.Thread(target=Capital,args = (stringi,));
    t3 = threading.Thread(target=Digits,args=(stringi,));

    t1.start();
    t2.start();
    t3.start();

    t1.join();
    t2.join();
    t3.join();
