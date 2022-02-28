X = int(input())

prime_factor = []

def Factorization (N):
    limit = int(N**0.5)
    for i in range(2,limit+1):
        while N%i == 0:
            prime_factor.append(i)
            N /= i
    if N >= 2:
        prime_factor.append(int(N))

Factorization(X)
print(*prime_factor)