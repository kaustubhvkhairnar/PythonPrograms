#3. Write a program which contains one function named as Add() which accepts two numbers
#from user and return addition of that two numbers.

def Add(num1,num2):
	return(num1+num2);
	
if __name__ == "__main__":
	ret=Add(num1=int(input("Enter first number")),num2=int(input("Enter second number")));
    
    print("Addition is",ret);
