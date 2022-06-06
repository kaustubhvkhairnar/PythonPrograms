#1.Design python application which creates two thread named as even and odd. Even
#thread will display first 10 even numbers and odd thread will display first 10 odd
#numbers.

import threading;

def even(no):

	for i in range(no):
		if ((i % 2) == 0):
			print("Even : ",i);


def odd(no):
	for i in range(no):
		if(i % 2 != 0):
			print("Odd : ",i);


if __name__ == "__main__":
	num = 20;
	t1 = threading.Thread(target = even,args = (num,));
	t2 = threading.Thread(target = odd,args = (num,));

	t1.start();
	t1.join();

	t2.start();
	t2.join();
