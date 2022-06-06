#11. Write a program which accept number from user and return addition of digits in that number.

def fun(num):
    sum=0
    while (num!=0):
        one=num%10
        num=num//10
        sum=sum+one
    print("Number of digits :",sum)

if __name__ == "__main__":
    fun(num=int(input("Enter number : ")))
