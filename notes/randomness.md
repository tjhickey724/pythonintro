# Randomness
Python gives us access to pseudorandom number generators via the ```random```package.

For example random.randint(a,b) will return random integers x with a<=x<=b

Here is an example of printing a random k-digit PIN
``` python
from random import randint

def print_pin(k):
    ''' create a pin with k random digits 0-9 '''
    for i in range(k):
        print(randint(0,9),end='')
    print()
```


