def sum_pair(numbers, target_sum):
    num_set = set()

    for num in numbers:
        complement = target_sum - num

        if complement in num_set:
            return (num, complement)
        
        num_set.add(num)

    return None


input_numbers = list(map(int, input("Enter a list of numbers: ").split()))
target = int(input("Enter the target sum: "))

pair = sum_pair(input_numbers, target)

if pair:
    print(f"Yes, {target} = {pair[0]} + {pair[1]}")
else:
    print("No")
