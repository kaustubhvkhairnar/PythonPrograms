#4.Write a program which accept N numbers from user and store it into List. Accept one another
#number from user and return frequency of that number from List.

def main():
    num = int(input("Enter number of elements : "))
    fun(num);

def fun(no):
    print("Enter", no, "Element/s");
    arr = [];
    for i in range(no):
        print("Enter", i + 1, "element");
        num = int(input());
        arr.append(num);

    max = arr[0];
    cnt=0;
    
    sam = int(input("Enter the number whose frequency you want to search : "))
    
    for i in range(no):
        if (arr[i] == sam):
            cnt=cnt+1;

    print("Given elements : ", arr);
    print("Frequency of number ",num," is : ",cnt);


if __name__ == "__main__":
    main();
