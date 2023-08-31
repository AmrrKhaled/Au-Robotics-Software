string_1=input("Enter first Word: ")
string_2=input("Enter second Word: ")
checker=[0]*len(string_1)
if (len(string_1)==len(string_2)):
    for char_1 in string_1:
    
        for i in range(len(string_2)):
            if string_2[i]==char_1 and checker[i] == 0:
                checker[i]=1
                break               

print(checker)   
   
                
if checker.count(1) == len(string_1):
        print("Anagram")
else:
        print("NOT Anagram")