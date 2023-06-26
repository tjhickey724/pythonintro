# Tuples and Mutability
In Python, a tuple is a data structure very similar to a list 
It main differences are that 
* it is defined using parentheses (10,20,30) rather than square brackets [10,20,30]
``` python
  tuple_vals=(10,20,30,40,50)
  list_vals = [10,20,30,40,50]
```
* you can access the elements of a tuple with indexing and slicing
  ``` python
  print(tuple_vals[1]) --> prints 20
  print(tuple_vals[1:-1]) --> prints (20,30,40)
  ```
* Bur, it is immutable,
  that is, you cannot assign a different value to an index of a tuple.
``` python
  tuple_vals[1]=21  # this generates a run-time error!!
  list_vals[1] = 21 # this changes the second element of list_val to 21, with no errors
```
It is similar in that it can store a sequence of data and

* you can iterate through a tuple with a for loop
``` python
for d in tuple_vals:
  print(d, end=" ")
```


You can convert between lists and tuples using the ```list(T)``` and ```tuple(L)``` functions
```
> x=[1,2,3]
> y=tuple(x) # stores the tuple (1,2,3) in y
> z = list(y)   # returns the list [1,2,3] in z
> print(x,y,z)
[1,2,3]  (1,2,3)  [1,2,3]
```
