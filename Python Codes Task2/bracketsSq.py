string_1=list(input("Enter brackets sequence: "))
openBrackets=0
closedBrackets=0
for i in range (len(string_1)):
    if string_1[i] == '(':
       openBrackets+=1 
       for j in range (len(string_1)):
           if string_1[j] == ')' and j > i :
              string_1[j]='*'
              closedBrackets+=1
              break        
# print(string_1)
# print(openBrackets)
# print(closedBrackets)
if(openBrackets+closedBrackets==len(string_1) and openBrackets==closedBrackets):
    print("Valid")
else:
    print("Invalid")




