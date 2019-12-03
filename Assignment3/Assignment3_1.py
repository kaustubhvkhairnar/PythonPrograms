#1.Write a program which accept N numbers from user and store it into List. Return addition of all
#elements from that List.

def main():
	num=int(input("Enter number of elements"))
	fun(num);

	
def fun(no):
	print("Enter",no,"Element/s");
	arr =[];
	sum=0;
	for i in range(no):
		print("Enter",i+1,"element");
		num=int(input());
		arr.append(num);
		sum=sum+num;
	print("Given elements : ",arr);
	print("Sum of the elements : ",sum);

if __name__=="__main__":
	main();
