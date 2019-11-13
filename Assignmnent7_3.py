#3. Write a program which contains one class named as Numbers.
#Arithmetic class contains one instance variables as Value.
#Inside init method initialise that instance variables to the value which is accepted from user.
#There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),
#Factors().
#ChkPrime() method will returns true if number is prime otherwise return false.
#ChkPerfect() method will returns true if number is perfect otherwise return false.
#Factors() method will display all factors of instance variable.
#SumFactors() method will return addition of all factors. Use this method in any another method
#as a helper method if required.
#After designing the above class call all instance methods by creating multiple objects.

class Numbers:

    def __init__(self,no):
        self.value=no ;

    def ChkPrime(self):
        flag = 0;
        for i in range(2, self.value):
            if (self.value % i == 0):
                flag = 1;
                break;
        if (flag == 1):
            return False;
        else:
            return True;

    def ChkPerfect(self):
        res = Numbers.SumFactors(self);
        if(res== self.value):
            return True;

    def SumFactors(self):
        sum=0;
        fact = Numbers.Factors(self);
        for i in range(len(fact)):
            sum = sum + fact[i];
        return sum;

    def Factors(self):
        arr=list();
        for i in range(1,self.value):
            if(self.value%i==0):
                arr.append(i);
        return arr;

def main():
    no = input("Enter Number : ");
    obj = Numbers(int(no));
    ret1 = obj.ChkPrime();
    if(ret1==True):
        print (no,"is prime number.")
    else:
        print (no, "is not a prime number.")

    ret2 = obj.ChkPerfect();
    if (ret2 == True):
        print (no, "is perfect number.")
    else:
        print (no, "is not a perfect number.")

    ret3 = obj.SumFactors();
    print ("Sum of factors is ",ret3);

    ret4 = obj.Factors();
    print("Factors of ",no,"are",ret4);

if __name__  == "__main__":
    main();