from random import randint

vals = [randint(0,100000) for _ in range(10000)]
print(vals[:10])
vals = sorted(vals)
print(vals[:10],vals[-10:])
# is 5207 in the list vals of length 100,000?
'''

vals[5000]  50343 look before that index
vals[2000] 19942
vals[1000] 9778
vals[500] 4792  so 5207 index is between 500 and 1000
vals[750] 7459    lo=500 hi=750
vals[560] 5371   lo =500 hi =560
vals[540] 5159  want 5207 lo=540 hi=560
vlas[550] 5245   lo=540 hi=550
vals[545] = 5182  lo 545 hi 550
vals[547] = 5204  lo 547 hi 550
vals[548] = 5205 lo 548 hi 550
vals[549]=5240 so 5207 is not in the list (12 steps)




'''[]