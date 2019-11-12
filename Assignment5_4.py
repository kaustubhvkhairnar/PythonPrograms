#4.Write a recursive program which accept number from user and return
#summation of its digits.

sum=0;

def main():
    value=input("Enter number : ")
    rec4(int(value));
    print (sum);


def rec4(no):
    global sum;
    if(no!=0):
        rem=no%10;
        sum=sum+rem;
        no=no//10;
        rec4(no);



if __name__ == "__main__":
    main();