#5. Write a program which contains one class named as BankAccount.
#BankAccount class contains two instance variables as Name & Amount.
#That class contains one class variable as ROI which is initialise to 10.5.
#Inside init method initialise all name and amount variables by accepting the values from user.
#There are Four instance methods inside class as Display(), Deposit(), Withdraw(),
#CalculateIntrest().
#Deposit() method will accept the amount from user and add that value in class instance variable
#Amount.
#Withdraw() method will accept amount to be withdrawn from user and subtract that amount
#from class instance variable Amount.
#CalculateIntrest() method calculate the interest based on Amount by considering rate of interest
#which is Class variable as ROI.
#And Display() method will display value of all the instance variables as Name and Amount.
#After designing the above class call all instance methods by creating multiple objects.

class BankAccount:

    ROI = 10.5

    def __init__(self,value1,value2):
        self.Name = value1
        self.Amount = value2

    def Display(self):
        print("Name : ",self.Name)
        print("Amount : ",self.Amount)

    def Deposit(self,value):
        self.Amount = self.Amount+value

    def Withdraw(self,value):
        self.Amount = self.Amount - value

    def CalculateInterest(self,value):
        Rate = value + BankAccount.ROI//100
        print("Rate of interest for ",value,"is",Rate)

def main():
    obj = BankAccount("Kaustubh",int(200000))
    obj.Display()
    obj.Deposit(int(200))
    print("Deposting")
    obj.Display()
    obj.Withdraw(int(300))
    print("Withdrawing")
    obj.Display()
    obj.CalculateInterest(int(30000))

if __name__=="__main__":
    main()
