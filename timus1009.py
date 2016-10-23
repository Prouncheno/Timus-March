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


print(K_based_numbers(N, K))
