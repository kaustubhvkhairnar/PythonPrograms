#1.Write a program which contains one lambda function which accepts one parameter and return power of two.

def main():
    value=input("Enter number : ")
    ret=fp(value);
    print(ret)

fp=lambda no : int(no) **2;

if __name__=="__main__":
    main();
