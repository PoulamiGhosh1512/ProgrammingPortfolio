


'''
Karatsuba's Algorithm-A Fast Multiplication Algorithm
x,y:input numbers
n:no. of digits in input numbers
10:base of input numbers
'''
def FastMultiply(x,y,n):
    if n == 1:
        return x * y
    else:
        m = n/2
        xh = x//10**m
        xl = x % (10**m)
        yh = y//10**m
        yl = y % (10**m)
        a = xh + xl
        b = yh + yl
        p = FastMultiply(xh, yh, m)
        q = FastMultiply(xl, yl, m)
        r = FastMultiply(a, b, m)
        return p*(10**n) + (r - q - p) * (10**(n/2)) + q 
print(FastMultiply(1234,5678,4))
