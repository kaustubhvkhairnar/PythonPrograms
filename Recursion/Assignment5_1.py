#1. Write a recursive program which display below pattern.
#Input :  5
#Output : * * * * *

def main():
    value=input("Enter number : ")
    rec1(int(value));

def rec1(no):
    if(no!=0):
        print("*",end=' ');
        no=no-1;
        rec1(no);

if __name__ == "__main__":
    main();
