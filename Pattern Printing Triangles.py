def main():
    def right_triangle():
        n=int(input("Enter the number of rows: "))
        for i in range(n):
            for j in range(i + 1):
                print("*", end=" ")
            print()
    def rev_right_triangle():
        n=int(input("Enter the number of rows: "))
        for i in range(n, 0, -1):
            for j in range(i):
                print("*", end=" ")
            print()
    def pyramid():
        n=int(input("Enter the number of rows: "))
        for i in range(n):
            for j in range(n - i - 1):
                print(" ", end="")
            for j in range(2 * i + 1):
                print("*", end="")
            print()
    def rev_pyramid():
        n=int(input("Enter the number of rows: "))
        for i in range(n, 0, -1):
            for j in range(n - i):
                print(" ", end="")
            for j in range(2 * i - 1):
                print("*", end="")
            print()
    print("Choose a pattern to print:")
    print("1. Right Triangle")
    print("2. Reverse Right Triangle")
    print("3. Pyramid")
    print("4. Reverse Pyramid")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        right_triangle()
    elif choice == '2':
        rev_right_triangle()
    elif choice == '3':
        pyramid()
    elif choice == '4':
        rev_pyramid()
    else:
        print("Invalid choice!")
if __name__ == "__main__":
    main()
    