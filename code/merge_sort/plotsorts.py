from bubblesort import *
from mergesort import *
from matplotlib import pyplot as plt

for n in [1,10,100,1000]:
    print('n=',n,'mergesort=',MStimetest(n),'bubblesort=',BStimetest(n))



xs = [1,100,200,300,400,500,1000]
ms = [MStimetest(n) for n in xs]
plt.plot(xs,ms,label='mergesort')
bs = [BStimetest(n) for n in xs]
plt.plot(xs,bs,label='bubblesort')
plt.grid()
plt.xlabel("size n of list")
plt.ylabel("seconds to sort the list")
plt.title("comparison of mergesort and bubblesort times")
plt.show()
plt.legend()
print('done')

n=1000
t = MStimetest(n)
ns = [n]
ts = [t]
print(n,t)
while t<1:
    n=n*2
    t = MStimetest(n)
    ns.append(n)
    ts.append(t)
    print(n,t)
plt.plot(ns,ts)
plt.show()

