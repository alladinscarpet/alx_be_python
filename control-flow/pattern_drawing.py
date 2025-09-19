size = int(input("Enter the size of the pattern: "))

curr_row = 0

while curr_row < size:
    for i in range(size):
        print("*", end="")
    print()

    curr_row += 1