#5. Write a recursive program which accept number from user and return its
#factorial.

def main():
    value=input("Enter number : ")
    fact=factorial(int(value));
    print(fact)

def factorial(no):
    if no == 1:
        return 1
    else:
        return no * factorial(no-1)

if __name__ == "__main__":
    main();