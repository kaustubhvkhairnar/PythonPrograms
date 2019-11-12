# 2. Write a program which contains one class named as Circle.
# Circle class contains three instance variables as Radius ,Area, Circumference.
# That class contains one class variable as PI which is initialise to 3.14.
# Inside init method initialise all instance variables to 0.0.
# There are three instance methods inside class as Accept(), CalculateArea(), CalculateCircumference(), Display().
# Accept method will accept value of Radius from user.
# CalculateArea() method will calculate area of circle and store it into instance variable Area.
# CalculateCircumference() method will calculate circumference of circle and store it into instance variable Circumference.
# And Display() method will display value of all the instance variables as Radius , Area, Circumference.
# After designing the above class call all instance methods by creating multiple objects.

class Circle:
    PI = 3.14;

    def __init__(self):
        self.Radius = 0.0;
        self.Area = 0.0;
        self.Circumference = 0.0;

    def Accept(self):
        self.Radius = int(input("Enter Radius"))
        return self.Radius;

    @classmethod
    def CalculateArea(cls,Radius):
        Area = cls.PI * Radius * Radius;
        return (Area);


    @classmethod
    def CalculateCircumference(cls, Radius):
        print("Radius is ", Radius)
        print("cls.PI",cls.PI)
        Circumference = 2 * cls.PI * Radius;
        return (Circumference)

    def Display(self,Area,Circumference):
        print(self.Radius);
        print(Area);
        print("Circumference is ",Circumference)


def main():
    obj1 = Circle()
    ret = obj1.Accept();
    r1=obj1.CalculateArea(ret);
    r2=obj1.CalculateCircumference(ret);
    obj1.Display(r1,r2);

if __name__ == "__main__":
    main();
