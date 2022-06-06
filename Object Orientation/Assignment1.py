# 1.Write a program which contains one class named as Demo.
# Demo class contains two instance variables as no1 ,no2.  That class contains one class variable as Value.
# There are two instance methods of class as Fun and Gun which displays values of instance variables.
# Initialise instance variable in init method by accepting the values from user.
# After creating the class create the two objects of Demo class as
#   Obj1 = Demo(11,21) 
#   Obj2 = Demo(51,101) 
# Now call the instance methods as
#   Obj1.Fun() 
#   Obj2.Fun()
#   Obj1.Gun()
#   Obj2.Gun()

class Demo:

    Value = 100;

    def __init__(self, no1, no2):
        self.num1 = no1;
        self.num2 = no2;

    def Fun(self):
        print("Inside Fun ");
        print(self.num1);
        print(self.num2);
        print()

    def Gun(self):
        print("Inside Gun ");
        print(self.num1);
        print(self.num2);
        print()

def main():
    no1 = int(input("Enter First number For 1st obj : "));
    no2 = int(input("Enter Second number For 1st obj : "));
    Obj1 = Demo(no1, no2);

    no3 = int(input("Enter First number For 2nd obj : "));
    no4 = int(input("Enter Second number For 2nd obj : "));
    Obj2 = Demo(no3, no4);

    print ("Obj1.Fun() ");
    Obj1.Fun()
    print("Obj2.Fun() ");
    Obj2.Fun()
    print( "Obj1.Gun() ")
    Obj1.Gun()
    print("Obj2.Gun() ")
    Obj2.Gun()

if __name__ == "__main__":
    main();
