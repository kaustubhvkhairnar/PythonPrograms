#4.Write a program which contains one class named as BookStore.
#BookStore class contains two instance variables as Name ,Author.
#That class contains one class variable as NoOfBooks which is initialise to 0.
#There is one instance methods of class as Display which displays name , Author and number of books.
#Initialise instance variable in init method by accepting the values from user as name and author.
#Inside init method increment value of NoOfBooks by one.
#After creating the class create the two objects of BookStore class as
#Obj1 = BookStore(“Linux System Programming”, “Robert Love”)
#Obj1.Display() # Linux System Programming by Robert Love. No of books : 1
#Obj2 = BookStore(“C Programming”, “Dennis Ritchie”)
#Obj2.Display() # C Programming by Dennis Ritchie. No of books : 2

class BookStore:

    NoOfBooks = 0;

    def __init__(self,value1,value2):
        self.Name = value1;
        self.Author = value2;
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1;


    def info(self):
        print("Name : ",self.Name);
        print("Author : ",self.Author);
        print("Number of books : ",BookStore.NoOfBooks);

def main():
    print("Inside main");
    obj1 = BookStore("Linux System Programming", "Robert Love");
    obj1.info();
    obj2 = BookStore("C Programming", "Dennis Ritchie");
    obj2.info();

if __name__ == "__main__": #Starter
    main();
