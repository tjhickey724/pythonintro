def square_list(n):
    squares = [x*x for x in range(n+1)]
    return squares

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]
print(divisors(15))


