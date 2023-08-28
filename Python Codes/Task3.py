amount = int(input("Enter the amount in Egyptian Pounds: "))
paper_bills = [200, 100, 50, 20, 10, 5, 1]
bill_counts = {}

for i in paper_bills:
        count = amount // i
        if count > 0:
            bill_counts[i] = count
            amount %= i

for bill, count in bill_counts.items():
        print(f"{count}x {bill} L.E.")






