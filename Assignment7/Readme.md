# Object Orientation Using Python

Assignment7_1.py :-

It is a program which contains one class named as BookStore.
BookStore class contains two instance variables as Name ,Author.
That class contains one class variable as NoOfBooks which is initialise to 0.
There is one instance methods of class as Display which displays name , Author and number of books.
Initialise instance variable in init method by accepting the values from user as name and author.
Inside init method increment value of NoOfBooks by one.
After creating the class create the two objects of BookStore class as
Obj1 = BookStore(“Linux System Programming”, “Robert Love”)
Obj1.Display() # Linux System Programming by Robert Love. No of books : 1
Obj2 = BookStore(“C Programming”, “Dennis Ritchie”)
Obj2.Display() # C Programming by Dennis Ritchie. No of books : 2

Assignment7_2.py :-

It is a program which contains one class named as BankAccount.
BankAccount class contains two instance variables as Name & Amount.
That class contains one class variable as ROI which is initialise to 10.5.
Inside init method initialise all name and amount variables by accepting the values from user.
There are Four instance methods inside class as Display(), Deposit(), Withdraw(),
CalculateIntrest().
Deposit() method will accept the amount from user and add that value in class instance variable
Amount.
Withdraw() method will accept amount to be withdrawn from user and subtract that amount
from class instance variable Amount.
CalculateIntrest() method calculate the interest based on Amount by considering rate of interest
which is Class variable as ROI.
And Display() method will display value of all the instance variables as Name and Amount.
After designing the above class call all instance methods by creating multiple objects.

Assignment7_3.py :-

It is a program which contains one class named as Numbers.
Arithmetic class contains one instance variables as Value.
Inside init method initialise that instance variables to the value which is accepted from user.
There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),
Factors().
ChkPrime() method will returns true if number is prime otherwise return false.
ChkPerfect() method will returns true if number is perfect otherwise return false.
Factors() method will display all factors of instance variable.
SumFactors() method will return addition of all factors. Use this method in any another method
as a helper method if required.#After designing the above class call all instance methods by creating multiple objects.   
