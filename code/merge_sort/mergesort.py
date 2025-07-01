import random
import time

def merge(list1, list2):
    """ return the result of merging two sorted lists 
       the idea is we create a new list by taking the smallest value from the front of the two lists,
       and moving it onto the new list. Do this until one of the lists is empty, then copy the rest
       of the other list to the result.
    
    """
    result = []
    i = j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    # Add remaining elements of the non-empty list, to the end of the list
    # note that one of these two lists is empty, so the extend does nothing for that list
    result.extend(list1[i:])
    result.extend(list2[j:])
    
    return result

def mergesort(vals):
    ''' sort vals by recursively sorting 2 halves then merging '''
    n = len(vals)
    if n<=1: # a list of size 0 or 1 is already sorted
        return vals
    mid = n//2  # calculate the approximate midpoint
    return( merge(mergesort(vals[:mid]),mergesort(vals[mid:])))


def mergesort_v(vals):
    ''' verbose version which shows steps more clearly '''
    n = len(vals)
    if n<=1:
        return vals
    mid = n//2  # split into two halfs, roughly equal
    vs = vals[:mid]  # left half of the list, has length = mid
    ws = vals[mid:]  # right half of the list, has length = mid or mid+1
    vs = mergesort_v(vs) # sort the left half, recursively
    ws = mergesort_v(ws) # sort the right half, recursively
    vals = merge(vs,ws) # merge the sorted lists in about n steps
    return vals

def MStest(n):
    vals = [random.randint(0,10*n) for _ in range(n)]
    print('before sorting',vals)
    mergesort(vals)
    print('after sorting',vals)



def MStimetest(n):
    vals = [random.randint(0,10*n) for _ in range(n)]
    start = time.perf_counter_ns()
    mergesort(vals)
    end = time.perf_counter_ns()
    total = (end-start)/10**9 
    return total


if __name__=='__main__':
    
    n = int(input("n: "))
    while n>0:
        print('time in seconds:',MStimetest(n))
        n = int(input("n: "))

        
