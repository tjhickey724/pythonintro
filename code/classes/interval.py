'''
Intervals using Python classes
'''

class Interval():
    def __init__(self,a,b):
        self.lo = a
        self.hi = b
        
    def __str__(self):
        ''' converts the interval to a string '''
        return(f'[{self.lo},{self.hi}]')
    
    def __eq__(self,other):
        ''' test if this interval equals the other '''
        return self.lo==other.lo and self.hi==other.hi
    
    def width(self):
        ''' return the width of the interval '''
        return self.hi - self.lo
    
    def contains(self,x):
        ''' return true if x is in the interval '''
        return self.lo<=x<= self.hi