#2. Write a program which contains one function named as ChkNum() which accept one parameter as number.
# If number is even then it should display “Even number” otherwise display “Odd number” on console.

def chkNum(number):
	if number%2 == 0:
		print("Even Number");
	else:
		print("Odd Number");
		
if __name__ == "__main__":
	chkNum(int(input("Enter your number")));
