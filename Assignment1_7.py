# 7. Write a program which contains one function that accept one number from user and returns
# true if number is divisible by 5 otherwise return false.

def chkNum(number):
    if number % 5 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    number = int(input("Enter your number"))
    ret = chkNum(number)

    if ret == True:
        print(number, "is divisible by 5")
    else:
        print(number, "is not divisible by 5")
