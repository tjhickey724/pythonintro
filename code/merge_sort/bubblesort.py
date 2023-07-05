import random
import time

def bubblesort(vals):
    for i in range(len(vals)):
        for j in range(len(vals)-1):
            if vals[j]>vals[j+1]:
                # swap them
                #(vals[j],vals[j+1])=(vals[j+1],vals[j])
                tmp = vals[j]
                vals[j] = vals[j+1]
                vals[j+1] = tmp
                


def BStest(n):
    vals = [random.randint(0,10*n) for _ in range(n)]
    print('before sorting',vals)
    bubblesort(vals)
    print('after sorting',vals)

def BStimetest(n):
    vals = [random.randint(0,10*n) for _ in range(n)]
    start = time.perf_counter_ns()
    bubblesort(vals)
    end = time.perf_counter_ns()
    total = (end-start)/10**9
    return total


if __name__=='__main__':
    #BStest(20)
    n = int(input("n: "))
    while n>0:
        print('time in seconds:',BStimetest(n))
        n = int(input("n: "))
    