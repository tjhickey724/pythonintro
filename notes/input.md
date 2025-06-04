# Input
Python offers several ways to read data. The simplest is to print a prompt and ask the user to enter a value.
This is done with the ```input(PROMPT)``` method as follows:

``` python
# print greeting
user_name = input("What is your name?)
print("Hello",user_name,"How are you doing today?")
```

the ```input``` function always returns a string. If you want to do arithmetic on the input value
you need to convert it to an integer (with ```int(input(PROMPT))``` or a decimal number 
(with ```float(input(PROMPT))``` 

```python
# calculate age in years
age_in_years = float(input("How old are you?"))
age_in_days = 365.25 * age_in_years
print("you are",age_in_days,"days old")
```

If you only wanted 2 digits after the decimal point you could print using the f-string notation

```python
# calculate age in years
age_in_years = float(input("How old are you?"))
age_in_days = 365.25 * age_in_years
print(f"you are {age_in_days:.2f} days old")
```


