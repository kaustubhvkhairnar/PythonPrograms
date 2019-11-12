#2.Write a recursive program which display below pattern.
#Input :  5
#Output : 1 2 3 4 5
num=1;

def main():
    value=input("Enter number : ")
    rec2(int(value));

def rec2(no):
    global num;
    if(no!=0):
        print(num,end=' ');
        no=no-1;
        num=num +1;
        rec2(no);

if __name__ == "__main__":
    main();