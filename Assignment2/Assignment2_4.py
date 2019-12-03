#4.Write a program which accept one number form user and return addition of its factors.

def fun(num):
    sum=0;
    for n in range(num-1,0,-1):
        if(num%n==0):
            sum = sum + n;

    print("Addition of factors of number ",num,"is",sum)

if __name__ == "__main__":
    fun(num=int(input("Enter number : ")));
