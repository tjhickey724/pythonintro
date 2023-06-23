# Tuples and Mutability
In Python, a tuple is a data structure very similar to a list except that
* it is defined using parentheses (10,20,30) rather than square brackets [10,20,30]
  ``` python
  tuple_val=(10,20,30)
  list_val = [10,20,30]
* you can access the elements of a tuple with indexing and slicing
  ``` python
  print(tuple_val[1])
  print(tuple_val[1:-1])
  ```
* it is immutable, you cannot assign a different value to an index of a tuple.
  ``` python
  tuple_val[1]=21  # this generates a run-time error!!
  list_val[1] = 21 # this changes the second element of list_val to 21, with no errors
  ```

