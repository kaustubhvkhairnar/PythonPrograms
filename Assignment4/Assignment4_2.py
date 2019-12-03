#2.Write a program which contains one lambda function which accepts two parameters and return
#its multiplication.

def main():
    value1 = input("Enter number1 : ")
    value2 = input("Enter number2 : ")
    ret=fp(value1,value2);
    print(ret)

fp=lambda no1,no2 : int(no1)*int(no2);

if __name__=="__main__":
    main();
