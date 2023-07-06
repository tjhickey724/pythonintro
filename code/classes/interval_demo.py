'''
interval_demo shows how to use interval objects
'''

from interval import Interval

# Let's try working with Interval objects here
x = Interval(1,2)

print(x,'has width',x.width())


if x.contains(1.5):
    print(1.5,'is in',x)
else:
    print(1.5,'is not in',x)

y = Interval(1,3)
z = Interval(1,2)
print('x=',x)
print('y=',y)
print('z=',z)
print('x==y?',x==y)
print('x==z?',x==z)