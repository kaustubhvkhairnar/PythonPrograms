#3. Write a program which contains one class named as Arithmetic.  
#Arithmetic class contains three instance variables as Value1 ,Value2.  
#Inside init method initialise all instance variables to 0.  
#There are three instance methods inside class as Accept(), Addition(), Subtraction(), Multiplication(), Division(). 
#Accept method will accept value of Value1 and Value2 from user. 
#Addition() method will perform addition of Value1 ,Value2 and return result. 
#Subtraction() method will perform subtraction of Value1 ,Value2 and return result. 
#Multiplication() method will perform multiplication of Value1 ,Value2 and return result. 
#Division() method will perform division of Value1 ,Value2 and return result. 
#After designing the above class call all instance methods by creating multiple objects.

class Arithmetic:

    def __init__(self):
        self.Value1=0;
        self.Value2=0;

    def Accept(self):
        self.Value1 = int(input("Enter First Number"));
        self.Value2 = int(input("Enter Second Number"));

    def Addition(self,no1,no2):
        return no1+no2;

    def Subtraction(self,no1,no2):
        return no1-no2;

    def Multiplication(self,no1,no2):
        return no1*no2;

    def Division(self,no1,no2):
        return no1//no2;

def main():
    obj1= Arithmetic();
    obj1.Accept();
    obj1.Addition(Value1,Value2);
    obj1.Subtraction(Value1,Value2);
    obj1.Multiplication(Value1,Value2);
    obj1.Division(Value1, Value2);

    obj2=Arithmetic()
    obj2.Accept();
    obj2.Addition(Value1, Value2);
    obj2.Subtraction(Value1, Value2);
    obj2.Multiplication(Value1, Value2);
    obj2.Division(Value1, Value2);

if __name__ == "__main__":
    main();


