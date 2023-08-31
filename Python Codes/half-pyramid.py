
#After Updating

while True :
   row = int(input("Enter an integer range from 1 to 8: "))
   if row<=8 and row>0 :
     break
for i in range(1,row+1):
    print(' '*(row-i)+'#'*i,'','#'*i)



#  Before updating

# while True:
#     row = input("Enter an integer range from 1 to 8: ")
#     if  (1 <= int(row) <= 8):
#         break

# col = int(row) - 1
# col_hashes = 1

# for _ in range(0, int(row)):
    
#     for _ in range(0, col):
#         print(" ", end="")

    
#     for _ in range(0, col_hashes):
#         print("#", end="")

    
#     print("  ", end="")

    
#     for _ in range(0, col_hashes):
#         print("#", end="")

    
#     print()
#     col_hashes = col_hashes + 1
#     col = col - 1
