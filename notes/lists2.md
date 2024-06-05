# More Advanced List Operations
Return to this when we learn about loops!
  
## Accumulation loops
It is very common to uses lists for accumulation.
``` python
poem = ['Two', 'roads', 'diverged', 'in', 'a', 'yellow', 'wood']
long_words=[]
for word in poem:
  if len(word)>=4:
    long_words.append(word)
print(long_words)
```
will print
```
['roads','diverged','yellow','wood']
```

## Reading a list of positive numbers from the user
or we can read numbers from the user and store them in a list:
``` python
x=-1
numbers=[]
done=False
while not done:
  x = float(input("Enter a positive number, 0 to stop: "))
  if x>0:
    numbers.append(x)
  else:
    done=True
print('you entered',numbers)
print('the average is',sum(numbers)/len(numbers))
```

## Reading a list of arbitrary numbers
We can create a similar loop but ask the user if they want to continue at teach step
```
numbers=[]
response = 'y'
while response=='y':
    x = float(input("Enter a number: "))
    numbers.append(x)  # or numbers += [x]
    response = input("continue? (y or n) ")
print('you entered',numbers)
print('the average is',sum(numbers)/len(numbers))
```
  
