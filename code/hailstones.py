def next_hailstone(n):
    if n%2==0:  # n is even
        return n//2   # integer division by 2
    else:  # n is odd
        return 3*n+1
