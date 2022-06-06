# 9. Write a program which display first 10 even numbers on screen.

def main():
    for n in range(1, 21):
        if n % 2 == 0:
            print(n)

if __name__ == "__main__":
    main()
