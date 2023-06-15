largest = float('-inf')
smallest = float('inf')
total = 0
count = 0

x = float(input("Enter a positive value: "))

while x > 0:
    if x > largest:
        largest = x
    if x < smallest:
        smallest = x
    total += x
    count += 1
    x = float(input("Enter a positive value (0 to stop): "))

if count > 0:
    average = total / count
else:
    average = 0