numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []


def is_prime(n):
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                primes.append(n)
    else:
        not_primes.append(n)


print('Primes:', primes)
print('Not Primes:', not_primes)
