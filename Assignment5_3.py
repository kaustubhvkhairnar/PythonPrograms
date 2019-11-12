#3.Write a recursive program which display below pattern.
#Input :  5
#Output : 5 4 3 2 1

def main():
    value=input("Enter number : ")
    rec1(int(value));

def rec3(no):
    if(no!=0):
        print(no,end=' ');
        no=no-1;
        rec3(no);

if __name__ == "__main__":
    main();