def is_prime(n):
    if n < 2 : return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

def primes():
    yield 2
    i = 3
    while True:
        if is_prime(i):
            yield i 
        i += 2