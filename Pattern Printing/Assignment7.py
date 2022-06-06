#7. Write a program which accept one number and display below pattern.
#Input : 5
#Output :  1 2 3 4 5
#               1 2 3 4 5
#               1 2 3 4 5
#               1 2 3 4 5
#               1 2 3 4 5
def fun(number):
    for i in range(1,number):
        for n in range(1,number+1):
             print(n,end=' ')
        print()

if __name__ == "__main__":
    fun(number=int(input("Enter number")))


