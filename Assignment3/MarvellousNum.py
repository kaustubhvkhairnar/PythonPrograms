def chkprime(no):
    flag = 0;
    for i in range(2, no ):
        if (no % i == 0):
            flag = 1;
            break;
    if (flag == 1):
        return False;
    else:
        return True;


