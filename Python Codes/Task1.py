while True:
    row = input("Enter an integer range from 1 to 8: ")
    if  (1 <= int(row) <= 8):
        break

col = int(row) - 1
col_hashes = 1

for _ in range(0, int(row)):
    
    for _ in range(0, col):
        print(" ", end="")

    
    for _ in range(0, col_hashes):
        print("#", end="")

    
    print("  ", end="")

    
    for _ in range(0, col_hashes):
        print("#", end="")

    
    print()
    col_hashes = col_hashes + 1
    col = col - 1
