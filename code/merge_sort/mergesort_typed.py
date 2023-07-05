'''
this has been annotated with types to provide type checking!
'''
import random
import time
from typing import List

def merge(vs:List[float],ws:List[float])->List[float]:
    i=0
    j=0
    vals=[0.0]*(len(vs)+len(ws))
    while (i<len(vs) and j<len(ws)):
        if vs[i]<ws[j]:
            vals[i+j]=vs[i]
            i=i+1
        else:
            vals[i+j]=ws[j]
            j=j+1
    # either i==len(vs) or j== len(ws)
    # one of the lists has been fully processed

    # copy rest of ws to list
    while j<len(ws):
        vals[i+j]=ws[j]
        j=j+1
    # copy rest of vs to list
    while i<len(vs):
        vals[i+j]= vs[i]
        i=i+1
    return vals

def mergesort(vals:List[float])->List[float]:
    ''' sort vals by recursively sorting 2 halves then merging '''
    n = len(vals)
    if n<=1: # a list of size 0 or 1 is already sorted
        return vals
    mid = n//2
    return( merge(mergesort(vals[:mid]),mergesort(vals[mid:])))



vals = list(set([random.randint(1,1000) for i in range(100)]))
random.shuffle(vals)
print(vals)

print(sorted(vals)[:10])


  

def mergesort_v(vals:List[float]):
    ''' verbose version which shows steps more clearly '''
    n = len(vals)
    if n<=1:
        return vals
    mid = n//2  # split into two halfs, roughly equal
    vs = vals[:mid]
    ws = vals[mid:]
    vs = mergesort_v(vs) # sort those two halves, recursively
    ws = mergesort_v(ws)
    vals = merge(vs,ws) # merge the sorted lists in about n steps
    return vals

def MStest(n:int):
    vals = [random.randint(0,10*n) for _ in range(n)]
    print('before sorting',vals)
    vals = mergesort(vals)
    print('after sorting',vals)



def MStimetest(n:int)-> float:
    vals = [random.randint(0,10*n) for _ in range(n)]
    start = time.perf_counter_ns()
    vals = mergesort(vals)
    end = time.perf_counter_ns()
    total = (end-start)/10**9 
    return total


if __name__=='__main__':
    
    n = int(input("n: "))
    while n>0:
        print('time in seconds:',MStimetest(n))
        n = int(input("n: "))

        