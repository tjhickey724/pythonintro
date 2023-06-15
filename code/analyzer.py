x = float(input("Enter a positive value: "))
biggest_so_far = x
smallest_so_far = x
count = 0
sum = 0
while x > 0:
    count += 1
    sum += x
    if x > biggest_so_far:
        biggest_so_far = x
    elif x < smallest_so_far:
        smallest_so_far = x
    x = float(input("Enter a positive value (0 to stop):"))
print('the biggest number was',biggest_so_far)
print('the smallest number was', smallest_so_far)
print('the count is',count)
print('the range is',biggest_so_far-smallest_so_far)
print('the average is', sum / count)