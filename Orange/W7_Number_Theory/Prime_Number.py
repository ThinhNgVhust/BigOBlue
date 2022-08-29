def is_prime(n):
    # O(n)
    n = int(n ** 0.5) + 1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def eratosthenes(n):
    # return list of prime number less than or equal N
    # NloglogN
    mark = [True] * (n + 1)
    mark[0] = False
    mark[1] = False
    i = 2
    while i * i <= n:
        if mark[i] is True:
            for j in range(int(i * i), n + 1, i):
                mark[j] = False
        i += 1
    ans = []
    for i in range(len(mark)):
        if mark[i]: ans.append(i)
    return ans


def segmented_eratosthenes(left, right):
    # return list of prime numbers p that left<=p<=right
    # right <=1e12, right-left <=1e6
    primes = eratosthenes(int(right ** 0.5))
    if left == 1: left += 1
    mark = [True] * (right - left + 1)
    for i in range(len(primes)):
        if primes[i] > int(right ** 0.5): break
        base = (left // primes[i]) * primes[i]
        if base < left: base += primes[i]
        for j in range(base, right + 1, primes[i]):
            if j != primes[i]: mark[j - left] = False
    ans = []
    for i in range(left, right + 1):
        if mark[i - left] == True: ans.append(i)
    return ans


def phi(n):
    result = n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            result = ((i - 1) * result) // i
    if n > 1:
        result = ((n - 1) * result) // n
    return result


print(phi(7654321))


def prime_factor(n):
    tmp = n
    ans = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n = n // i
            ans.append(i)
        i += 1
    if n > 1: ans.append(n)
    phi = tmp
    for e in ans:
        phi = phi * (e - 1) // e
    print(phi)
    return ans


print(prime_factor(int(7654321)))
