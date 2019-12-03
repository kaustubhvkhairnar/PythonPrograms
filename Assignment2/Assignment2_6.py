#6. Write a program which accept one number and display below pattern.
#Input : 5
#Output : * * * * *
#              * * * *
#              * * *
#              * *
#              *

def fun(number):
    for n in range(number):
        for n in range(number):
             print("*",end=" ")
        print()
        number=number-1

if __name__ == "__main__":
    fun(number=int(input("Enter number : ")))


