import random


def bs_recursion(val,vals,start,end):
    if start==end: # Amy's case, the base case
        if val==vals[start]:
            return start
        else:
            return -1 
    else:  #recursion case
        mid = (start+end)//2
        midval = vals[mid]
        if midval==val:
            return mid
        elif val<midval:
            index = bs_recursion(val,vals,start,mid-1)
            return index
        else: # midval<val
            index = bs_recursion(val,vals,mid+1,end)
            return index

thelist = sorted([random.randint(1,100) for i in range(10)])
print(thelist)
val = random.choice(thelist)
index = bs_recursion(val,thelist,0,len(thelist)-1)
print(val,index)



