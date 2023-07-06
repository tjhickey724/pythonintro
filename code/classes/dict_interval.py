'''
Intervals using dictionaries
'''

def make_interval(a,b):
    return {'lo':a, 'hi':b}

def width(t):
    return t['hi'] - t['lo']

def contains(t,x):
    ''' true if interval t contains the point x '''
    return t['lo'] <= x <= t['hi']


y = make_interval(2,5)
#  same as y = {'lo':2,'hi':5}

w = width(y)

print(y['lo'], y['hi'],'has width', w)

if contains(y,1.5):
    print(1.5,'is in',y)
else:
    print(1.5,'is not in',y)
    
