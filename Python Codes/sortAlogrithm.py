list = [6, 8, 3, -8, 4, 7, 2,-99,-3,0,122,2]

for i in range(len(list)):
    min_value = list[i]
    min_index = i
    for j in range(i + 1, len(list)):
        if min_value > list[j]:
            min_value = list[j]
            min_index = j
    
    list[i], list[min_index] = list[min_index], list[i]

print(list)

