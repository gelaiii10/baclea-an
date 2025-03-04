odd_count = 0

for i in range(10):
    num = int(input(f"Enter Number {i + 1}: "))
    if num % 2 != 0:
        odd_count += 1

print(odd_count)