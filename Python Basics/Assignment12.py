#12. Write a program which accept number from user and return number of digits in that number.

def fun(num):
    sum=0
    while (num!=0):
        num=num//10
        sum=sum+1
    print("Number of digits :",sum)

if __name__ == "__main__":
    fun(num=int(input("Enter number : ")))
