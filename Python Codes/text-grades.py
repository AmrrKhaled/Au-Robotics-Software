string =input("Enter a text and show me your skill: ")
letters=0
sentences=0
words=0

for i in range(0, len(string)):
        if string[i].isalpha():
                letters += 1
        elif   string[i]=='!' or string[i]=='.' or string[i]=='?':
                sentences +=1
                words +=1
        
        elif string[i]==' ' and not(  string[i-1]=='!' or string[i-1]=='.'):
                words +=1

grade =  0.0588 * (letters/words*100) - 0.296 * (sentences/words*100) - 15.8


if grade>16:
     print("Grade 16+")
elif grade <1:
    print("Before Grade 1")
else:
    print("Grade:",round(grade))
    