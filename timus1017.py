from sys import stdin

n = int(stdin.readline())
result = n * [n * [0]]
i = n-1 # for h-1
j = n-1 # for n-1

# Rewrite the below function into a dual-circle with n*n space
while i >= 0:
    j = n - 1
    while j >= 0:
        if i+1 > (j+1)/2 and i <= j:
            result[i][j] = 1
        if i+1 <= (j+1)/2:
            result[i][j] = result[i+1][j] + result[i+1][j-i-1]
        j -= 1
    i -= 1

# The Kinds of n Bricks' Arrangment, and the least height is h
"""def KBA(h, n):
    if h > n:
        return 0
    elif h > n / 2:
        return 1
    else:
        return KBA(h+1, n) + KBA(h+1, n-h)
"""
print result[0][n-1] - 1
