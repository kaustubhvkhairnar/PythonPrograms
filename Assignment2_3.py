# 3. Write a program which accept one number from user and return its factorial.

def fun(num):
    fact = 1;
    if num < 0:
        print("Factorial Of negative number doesn't exists.");
    elif num == 0:
        print ("Factorial of 0 is 1.");
    for n in range(1, num + 1):
        fact = fact * n;
    print ("Factorial of given number", num, "is", fact);


if __name__ == "__main__":
    fun(num=int(input("Enter number : ")));
