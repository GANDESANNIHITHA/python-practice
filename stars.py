rows = int(input("Enter number of stars:"))
for i in range(rows, 0, -1):
    print("  "* (rows - i) + " *" * i)
for i in range(2, rows + 1):
    print("  "* (rows - i) + " *" * i)