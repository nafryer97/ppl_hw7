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

def square_primes():
    yield 2*2
    i = 3
    while True:
        if is_prime(i):
            yield i*i
        i += 2

#square_generator = square_primes()

#for i in square_generator:
#    print (i)

def is_spsp(n):
    if n < 6: return False
    elif n == 6: return True
    else:
        for x in square_primes():
            if x >= n: return False
            elif is_prime(n - x): return True

def spsp_nums(n):
    if is_spsp(n+1): yield (n + 1)
    else:
        i = n + 2
        while True:
            if is_spsp(i):
                yield i
            i += 1

student_id = 113387301 * 10

x = 0;

for i in spsp_nums(student_id):
    print i
    x += 1
    if x > 9:
        break