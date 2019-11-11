#6.Write a program which accept number from user and check whether that number is positive or
#negative or zero.

def fun(num):
	if num>0:
		print("Positive Number");
	elif num<0:
		print("Negative number");
	else:
		print("Zero");

if __name__ == "__main__":
	fun(int(input("Enter Number : ")));
		
