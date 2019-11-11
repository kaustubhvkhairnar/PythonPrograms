#8. Write a program which accept number from user and print that number of “*” on screen.

def fun(number):
    for n in range(number):
        print("*")

if __name__ == "__main__":
    number = int(input("Enter your number"))
    fun(number)	