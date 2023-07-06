'''
Intervals using Python classes
'''

class Interval():
    def __init__(self,a:float,b:float) -> None:
        self.lo:float = a
        self.hi:float = b
        
    def __str__(self):
        ''' converts the interval to a string '''
        return(f'[{self.lo},{self.hi}]')
    
    def __eq__(self,other) -> bool:
        ''' test if this interval equals the other '''
        return self.lo==other.lo and self.hi==other.hi
    
    def width(self) -> float:
        ''' return the width of the interval '''
        return self.hi - self.lo
    
    def contains(self,x:float):
        ''' return true if x is in the interval '''
        return self.lo<=x<= self.hi

x = Interval(1,2)
y = Interval(1,2)
print(x)
print(x==y)
print(x.width())
