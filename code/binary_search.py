import random

def binary_search(val,vals,start,end):
    while start<=end:
        mid = (start+end)//2
        print(start,mid,end,end-start)
        midval = vals[mid]
        if val==midval:
            return mid
        elif val<midval:
            end = mid-1
        else: # val>midval
            start = mid+1
    return -1

thelist = sorted([random.randint(1,10000) for i in range(1000)])
val = random.choice(thelist)  # pick a random elt from list
pos = binary_search(val,thelist,0,len(thelist)-1)
print(val,pos)
print(thelist[pos-4:pos+5])