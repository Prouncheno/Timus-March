from sys import stdin, stdout
N = int(stdin.readline())
K = int(stdin.readline())


def K_based_numbers(n, k):
    if n == 1:
        return k-1
    elif n == 2:
        return k * (k-1)
    else:
        return (k-1) * (K_based_numbers(n-1, k)+K_based_numbers(n-2, k))


i = 1
a = K - 1
b = K * (K - 1)
c = (K - 1) * (a + b)
if N == 1:
    print a
elif N == 2:
    print b
else:
    while i < N-1:
        c = (K - 1) * (a + b)
        a = b
        b = c
        i += 1
    print c
    
