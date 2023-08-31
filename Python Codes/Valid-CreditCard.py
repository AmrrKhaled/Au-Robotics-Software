cardNumber = input("Enter a Valid Credit Card Number: ")
cardNumber = list(cardNumber)
sum_1 = 0
sum_2 = 0
if len(cardNumber) == 16:
    divisor=0
else:
    divisor=1


for i in range(len(cardNumber) - 1, -1, -1):
    
    if i % 2 == divisor:
        product=int(cardNumber[i])*2
        if product<10:
            sum_1+=product
        else:
            sum_1+= (product//10)+(product%10)
    else:
        sum_2 += int(cardNumber[i])

checksum=(sum_1+sum_2)%10

if((cardNumber[:2] == ["3", "4"]) or (cardNumber[:2] == ["3","7"])) and checksum==0 and len(cardNumber)==15:
    print("American Express")
elif((cardNumber[:2] == ["5", "1"]) or (cardNumber[:2] == ["5","2"])or (cardNumber[:2] == ["5", "3"]) or (cardNumber[:2] == ["5","4"]) or (cardNumber[:2] == ["5","5"]) ) and checksum==0 and len(cardNumber)==16:
    print("MasterCard")
elif cardNumber[0] == "4" and checksum==0 and len(cardNumber)==16:
    print("Visa")
else:
    print("Invalid")    