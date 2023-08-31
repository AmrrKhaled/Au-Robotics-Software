numbers=[1,2,3,4,5,6,7,8,9,10]
def binarySearch(key,numbers,start=0,end = len(numbers) - 1):
    middle=(start+end)//2
    if  start <= end:
        if   key==numbers[middle]:
            return "Found"
        elif key > numbers[middle] :
             start = middle+1
             return binarySearch(key,numbers,start,end)
        else :
             end = middle-1
             return binarySearch(key,numbers,start,end)    
    else :
          return "NotFound"
x=int(input("Enter the key: "))
print(binarySearch(x,numbers))