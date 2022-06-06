#5.Write a program which accept one number for user and check whether number is prime or not.

def fun(num):
    if (num > 1):
        for a in range(2, num + 1):
            k=0
            for i in range(2, a // 2 + 1):
                if (a % i == 0):
                   k=k+1
        if (k <= 0):
            return True
        else:
            return False


if __name__ == "__main__":
    ret = fun(num=int(input("Enter number : ")))

    if ret == True:
        print ("Given number is Prime number")
    else:
        print("Given number is not a Prime number")
