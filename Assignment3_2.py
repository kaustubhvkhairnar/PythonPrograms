#2.Write a program which accept N numbers from user and store it into List. Return Maximum
#number from that List.

def main():
    num = int(input("Enter number of elements"))
    fun(num);

def fun(no):
    print("Enter", no, "Element/s");
    arr = [];
    for i in range(no):
        print("Enter", i + 1, "element");
        num = int(input());
        arr.append(num);

    max = arr[0];

    for i in range(no):
        if (arr[i] > max):
            max = arr[i];

    print("Given elements : ", arr);
    print("Maximum : ", max);


if __name__ == "__main__":
    main();
